# Instructor Notes: Scalable Data Processing

## LinkedIn Dataset

The Lecture Notebook and associated Homework use a synthetic LinkedIn dataset.  Note that the Lecture slides were run over a real instance of LinkedIn which, due to privacy concerns, is no longer publicly available.  We have therefore generated a synthetic dataset which is used for the associated Lecture Notebook, so the results will be different from those shown in the slides.

PUT INSTRUCTIONS HERE ON HOW THE INSTRUCTOR SHOULD OBTAIN THE DATASET. BE SURE TO WARN THAT THE NOTEBOOKS WILL NOT RUN IN THEIR CURRENT STATE, THE INSTRUCTOR MUST MODIFY ACCORDING TO WHERE THE DATASET IS.

This is what to do to make the data available to students:
PUT INSTRUCTIONS HERE ON HOW STUDENTS CAN USE THE DATA

## Creating a MongoDB server

There are two ways of doing this.  

* The instructor (or each student) sets up a MongoDB instance remotely by going to [mongodb.com](https://www.mongodb.com/).  Click on "Start free", sign up, agree to terms of service, and create a cluster. Use this location as 'Y' in the associated Lecture Notebook and Homework.  This option is required if students are working in Colab.

* Students create a local instance by installing MongoDB (see [1](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/) and [2](https://zellwk.com/blog/install-mongodb/)  for more details). The default server address is: mongodb://localhost:27017 . This option cannot be used if students are working in Colab. 
