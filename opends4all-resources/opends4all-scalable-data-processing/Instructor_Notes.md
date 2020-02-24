# Instructor Notes: Scalable Data Processing

The intended ordering of lessons in this module is 
1. [EFFICIENT-DATA-PROCESSING-architecture-algorithms-intermediate](EFFICIENT-DATA-PROCESSING-architecture-algorithms-intermediate.pptx)
2. [CLUSTER-DATA-PROCESSING-parallelism-partitioning-advanced](CLUSTER-DATA-PROCESSING-parallelism-partitioning-advanced.pptx) 
3. [CLUSTER-GRAPH-PROCESSING-centrality](CLUSTER-GRAPH-PROCESSING-centrality.pptx) 
4. [GRAPHS-adjacency-matrices](GRAPHS-adjacency-matrices.pptx)
5. [GRAPHS-PAGERANK-centrality](GRAPHS-PAGERANK-centrality.pptx)

## LinkedIn Dataset 

The Lecture Notebook and associated Homework use a synthetic LinkedIn dataset.  Note that the Lecture slides were run over a real instance of LinkedIn which, due to privacy concerns, is no longer publicly available.  We have therefore generated a synthetic dataset which is used for the associated Lecture Notebook, so the results will be different from those shown in the slides.

See instructions [here](opends4all-resources/opends4all-data-and-knowledge-modeling/Instructor_Notes.md) 
In addition to the data in data and knowledge modeling part, we are using the additional datasets: linkedin.edges.zip, linked.nodes.zip and stock_prices.csv. For best practice, instructors should make them available in an AWS S3 bucket, especially when AWS EMR cluster is used. 

## Creating a MongoDB server

See instructions [here](opends4all-resources/opends4all-data-and-knowledge-modeling/Instructor_Notes.md)


## Additional Resources

Instructors who want more depth on these topics can refer to

* For more on efficient data processing (SQL optimization, indexing, B+ trees) see relevant portions of a database textbook, e.g. ["Database Management Systems," by Ramakrishnan and Gehrke](https://docs.google.com/file/d/0B9aJA_iV4kHYM2dieHZhMHhyRVE/edit).  

* For more on cluster data and graph processing:
  * [Pandarize Your Spark DataFrames](https://lab.getbase.com/pandarize-spark-dataframes/)
  * [How Sharding Works](https://medium.com/@jeeyoungk/how-sharding-works-b4dec46b3f6#.9mndt52nc)
  * [Apache Spark](https://cacm.acm.org/magazines/2016/11/209116-apache-spark/abstract)
  * Tutorials on Spark, e.g. [for beginners](https://data-flair.training/blogs/what-is-spark/) or [more advanced](https://www.tutorialspoint.com/pyspark/index.htm)
  
* For more on centrality and PageRank
  * [PageRank](http://ilpubs.stanford.edu:8090/422/1/1999-66.pdf)
  * ["Data Science from Scratch" by Joel Grus](https://pdfs.semanticscholar.org/5a56/bbd762e9dd70dd20afe8740a6d09ec85ffed.pdf), Chapter 21 (Net Centrality).


