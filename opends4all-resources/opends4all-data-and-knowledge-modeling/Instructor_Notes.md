# Data and Knowledge Modeling

## Obtaining the LinkedIn Data
The Lecture Notebook and associated Homework use a LinkedIn dataset which was originally available on Kaggle.  However, due to privacy concerns it is no longer available. We have therefore created a synthetic dataset of 10k records for you to use in the Lecture Notebook and associated Homework. They are ‘linkedin_data_10000.zip’, ‘linkedin.nodes.new.zip’, and ‘linkedin.edges.zip’. 

There are two approaches to using this data:
1. Instructors make it available to students:
The instructor can download the zip file, unzip it (note that unzipping is optional since it can be done in the notebooks. ), put ‘linkedin_data_10000.json’, ‘linkedin.nodes’, and ‘linkedin_edges’ (or the zip files) on a server, and make the URL available to students.  Students can then use the python package ‘urllib’ to fetch the data. 

2. Provide zip files to students:
Make the zip files available to students, who can then unpack them. If students use Google Colab to run the notebook, then they must upload the files to their Google Drive and map the Google Drive to their Colab instance. The next step would be the same as running the notebook locally, where they put the data on a local computer and use the folder path to visit it. 

## Creating a MongoDB server
There are two ways of doing this.  

1.  The instructor (or each student) sets up a remote MongoDB instance by going to mongodb.com.  Click on "Get started", sign up, agree to terms of service, and create a cluster. Use this location as 'Y' in the associated Lecture Notebook and Homework.  **This option is required if students are working in Colab.**
2.  Students create a local instance by installing MongoDB (see instructions [here](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/) and [here](https://zellwk.com/blog/install-mongodb/)  for more details). The default server address is: mongodb://localhost:27017 . **This option cannot be used if students are working in Colab.**



## Additional Resources
Instructors who want more depth on this topic can refer to

* Knowledge graphs:  [ontologies](https://en.wikipedia.org/wiki/Ontology_(information_science) ) 

* Entity-Relationship (ER) model: [Wikipedia page](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) and relevant portions of this [textbook](https://docs.google.com/file/d/0B9aJA_iV4kHYM2dieHZhMHhyRVE/edit) "Database Management Systems," by Ramakrishnan and Gehrke.

* NoSQL: MongoDB [Tutorial](https://www.tutorialspoint.com/mongodb/mongodb_overview.htm)

* Transactions and concurrency: relevant portions of a basic database textbook, e.g. ["Database Management Systems"](https://docs.google.com/file/d/0B9aJA_iV4kHYM2dieHZhMHhyRVE/edit) by Ramakrishnan and Gehrke.  
