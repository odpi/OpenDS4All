import pandas as pd
import numpy as np

# JSON parsing
import json

# HTML parsing
from lxml import etree
import urllib

# SQLite RDBMS
import sqlite3

# Time conversions
import time

# Parallel processing
import swifter

# NoSQL DB
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, OperationFailure

import os

# TODO: Adapt the data loading code from class.

# YOUR CODE HERE
def get_df(rel):
    ret = pd.DataFrame(rel).fillna('')
    for k in ret.keys():
        ret[k] = ret[k].astype(str)
    return ret

def extract_relation(rel, name):
    '''
    Pull out a nested list that has a key, and return it as a list
    of dictionaries suitable for treating as a relation / dataframe
    '''
    # We'll return a list
    ret  = []
    if name in rel:
        ret2 = rel.pop(name)
        try:
            # Try to parse the string as a dictionary
            ret2 = json.loads(ret2.replace('\'','\"'))
        except:
            # If we get an error in parsing, we'll leave as a string
            pass
        
        # If it's a dictionary, add it to our return results after
        # adding a key to the parent
        if isinstance(ret2, dict):
            item = ret2
            item['person'] = rel['_id']
            ret.append(item)
        else:
            # If it's a list, iterate over each item
            index = 0
            for r in ret2:
                item = r
                if not isinstance(item, dict):
                    item = {'person': rel['_id'], 'value': item}
                else:
                    item['person'] = rel['_id']
                    
                # A fix to a typo in the data
                if 'affilition' in item:
                    item['affiliation'] = item.pop('affilition')
                    
                item['pos'] = index
                index = index + 1
                ret.append(item)
    return ret
    
def data_loading(file, dbname='linkedin.db', filetype='localobj', LIMIT=20000):

    if(filetype == 'localpath'):
        # linked_in = urllib.request.urlopen('file://' + cwd + '/' + file)
        linked_in = open(file)
    elif(filetype == 'localobj'):
        linked_in = file
    else: #URL
        linked_in = urllib.request.urlopen(file)

    names = []
    people = []
    groups = []
    education = []
    skills = []
    experience = []
    honors = []
    also_view = []
    events = []


    lines = []
    i = 0
    # LIMIT = 20000  # Max records to parse
    for line in file:
        try:
            line = line.decode('utf-8')
        except:
            line = line

        try:
            person = json.loads(line)

            # By inspection, all of these are nested dictionary or list content
            nam = extract_relation(person, 'name')
            edu = extract_relation(person, 'education')
            grp = extract_relation(person, 'group')
            skl = extract_relation(person, 'skills')
            exp = extract_relation(person, 'experience')
            hon = extract_relation(person, 'honors')
            als = extract_relation(person, 'also_view')
            eve = extract_relation(person, 'events')

            # This doesn't seem relevant and it's the only
            # non-string field that's sometimes null
            if 'interval' in person:
                person.pop('interval')

            lines.append(person)
            names = names + nam
            education = education + edu
            groups  = groups + grp
            skills = skills + skl
            experience = experience + exp
            honors = honors + hon
            also_view = also_view + als
            events = events + eve
        except:
            pass
        
        i = i + 1

        if(i % 10000 == 0):
            print (i)

        if i >= LIMIT:
            break


    people_df = get_df(pd.DataFrame(lines))
    names_df = get_df(pd.DataFrame(names))
    education_df = get_df(pd.DataFrame(education))
    groups_df = get_df(pd.DataFrame(groups))
    skills_df = get_df(pd.DataFrame(skills))
    experience_df = get_df(pd.DataFrame(experience))
    honors_df = get_df(pd.DataFrame(honors))
    also_view_df = get_df(pd.DataFrame(also_view))
    events_df = get_df(pd.DataFrame(events))

    recs_df = collect_peers_w_subset(people_df, skills_df)
    last_job_df = last_job(experience_df)

    conn = sqlite3.connect(dbname)


    # YOUR CODE HERE
    people_df.to_sql('people', conn, if_exists='replace', index=False)
    names_df.to_sql('names', conn, if_exists='replace', index=False)
    education_df.to_sql('education', conn, if_exists='replace', index=False)
    groups_df.to_sql('groups', conn, if_exists='replace', index=False)
    skills_df.to_sql('skills', conn, if_exists='replace', index=False)
    experience_df.to_sql('experience', conn, if_exists='replace', index=False)
    honors_df.to_sql('honors', conn, if_exists='replace', index=False)
    also_view_df.to_sql('also_view', conn, if_exists='replace', index=False)
    events_df.to_sql('events', conn, if_exists='replace', index=False)

    recs_df.to_sql('recs', conn, if_exists='replace', index=False)
    last_job_df.to_sql('lastjob', conn, if_exists='replace', index=False)

    return (people_df, names_df, education_df, groups_df, skills_df, experience_df, honors_df, also_view_df, events_df, recs_df, last_job_df)

# TODO: Find the top 15 skills for data scientists (Pandas)

def collect_peers(people_df_subset, skills_df, num):
    # YOUR CODE HERE
    ### BEGIN SOLUTION
    people_skills_df = people_df_subset.merge(skills_df, left_on='_id', right_on='person')[['_id','industry','value']]

    people_ids_df = people_df_subset[['_id']]
    people_ids_df.loc[:,'_id2'] = 0

    cartesian_df = people_ids_df.merge(people_ids_df,left_on='_id2',right_on='_id2')[['_id_x','_id_y']]
    cartesian_df = cartesian_df[cartesian_df['_id_x'] != cartesian_df['_id_y']]
    cartesian_df = cartesian_df.rename(columns={'_id_x': 'person_1', '_id_y': 'person_2'})

    recs_df = people_skills_df.merge(cartesian_df, left_on='_id', right_on='person_1').merge(people_skills_df, left_on=['person_2','value'], right_on=['_id','value'])[['person_1','person_2','value']].\
        groupby(by=['person_1','person_2']).count().reset_index().sort_values('value', ascending=False).head(num)

    return recs_df.rename(columns={"value":"common_skills"})
    ### BEGIN SOLUTION

def collect_peers_w_subset(people_df, skills_df):
    people_df_subset = people_df.head(100)
    return collect_peers(people_df_subset, skills_df, 20)

def last_job(experience_df):
    # YOUR CODE HERE
    # NOTE: limit the number of people returned, such that join ordering would make some sense here
    ### BEGIN SOLUTION
    return experience_df[experience_df['pos'] == '0'][['person','org','title']].sort_values('person').head(5000)
    ### END SOLUTION

def recommend_jobs(recs_df, names_df, last_job_df):
    # YOUR CODE HERE
    ### BEGIN SOLUTION
    return recs_df.merge(names_df,left_on='person_1',right_on='person')[['family_name','given_name','person_1','person_2']].\
        merge(last_job_df,left_on='person_2',right_on='person', how="left")[['family_name','given_name','person_2','org','title']].sort_values('family_name')
    ### END SOLUTION
