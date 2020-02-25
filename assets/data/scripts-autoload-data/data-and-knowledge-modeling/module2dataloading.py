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

'''
Simple code to pull out data from JSON and load into sqllite
'''
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

def data_loading(file, dbname='linkedin.db', filetype='localobj', LIMIT=100000):
    # cwd = os.getcwd()
    # print(cwd)
    
    if(filetype == 'localpath'):
        # linked_in = urllib.request.urlopen('file://' + cwd + '/' + file)
        linked_in = open(file)
    elif(filetype == 'localobj'):
        linked_in = file
    else: #URL
        linked_in = urllib.request.urlopen(file)

    START = 0
    # LIMIT = 100000

    names = []
    people = []
    groups = []
    education = []
    skills = []
    experience = []
    honors = []
    also_view = []
    events = []


    conn = sqlite3.connect(dbname)

    lines = []
    i = 1
    for line in linked_in:
        if i > START + LIMIT:
            # print(i, 'break')
            break
        elif i >= START:
            person = json.loads(line)

            # By inspection, all of these are nested dictionary or list content
            nam = extract_relation(person, 'name')
            edu = extract_relation(person, 'education')
            grp = extract_relation(person, 'group')
            skl = extract_relation(person, 'skills')
            exp  = extract_relation(person, 'experience')
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
            
        i = i + 1

        if(i % 10000 == 0):
            print (i)

    people_df = get_df(pd.DataFrame(lines))
    names_df = get_df(pd.DataFrame(names))
    education_df = get_df(pd.DataFrame(education))
    groups_df = get_df(pd.DataFrame(groups))
    skills_df = get_df(pd.DataFrame(skills))
    experience_df = get_df(pd.DataFrame(experience))
    honors_df = get_df(pd.DataFrame(honors))
    also_view_df = get_df(pd.DataFrame(also_view))
    events_df = get_df(pd.DataFrame(events))

    # Save these to an SQLite database

    people_df.to_sql('people', conn, if_exists='replace', index=False)
    names_df.to_sql('names', conn, if_exists='replace', index=False)
    education_df.to_sql('education', conn, if_exists='replace', index=False)
    groups_df.to_sql('groups', conn, if_exists='replace', index=False)
    skills_df.to_sql('skills', conn, if_exists='replace', index=False)
    experience_df.to_sql('experience', conn, if_exists='replace', index=False)
    honors_df.to_sql('honors', conn, if_exists='replace', index=False)
    also_view_df.to_sql('also_view', conn, if_exists='replace', index=False)
    events_df.to_sql('events', conn, if_exists='replace', index=False)

    # return (people_df, names_df, education_df, groups_df, skills_df, experience_df, honors_df, also_view_df, events_df)