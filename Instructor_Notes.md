# Instructor Notes

## Readings, Texts, and References

For the overall course, we recommend the following books as potentially being useful:

* Data Science from Scratch: First Principles with Python, 2nd ed, by Joel Grus, published by O'Reilly.

* Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython, 2nd ed, by Wes McKinney, published by O'Reilly.

Additionally, we recommend [Towards Data Science](towardsdatascience.com) as a useful resource for this space.

## Courses Using OpenDS4All Materials

* The University of Pennsylvania's CIS 545, Big Data Analytics, www.cis.upenn.edu/~cis545

## Background Material

Students may find the following resources to be useful as background:

* Google's Python class (free): https://developers.google.com/edu/python

* Harvard Online learning course on probability and statistics, https://online-learning.harvard.edu/course/introduction-probability-edx

## Suggested Configuration of Modules

The OpenDS4All modules can be "mixed and matched" at the discretion of the instructor, according to preferences, time constraints, and the target audience.  However, certain elements do have dependencies.  We suggest a "core" outline as follows:

1. [Overview](opends4all-resources/opends4all-overview), 1.5 lecture hours (basic)

   * _Optional recitation_: review of Python basics, including data structures

2. [Acquiring, wrangling, integrating, and cleaning data](opends4all-resources/opends4all-data-wrangling-and-integration), 3-4 lecture hours (basic-intermediate)

   * _Optional recitation_: basics of HTML and the Document Object Model
   * _Optional recitation_: basics of regular expressions (often used for pattern matching) and XPath (which builds on some ideas from regular expressions and traverses XML trees)

3. [Modeling data: types, graphs, schemas](opends4all-resources/opends4all-data-and-knowledge-modeling), 2-4 lecture hours

   * _Optional recitation_: encoding tree- or graph-structured data in relations, and traversing the data

4. [Understanding performance and scale](opends4all-resources/opends4all-scalable-data-processing), 4-8 lecture hours (intermediate, appropriate for a more computational and big data audience)

    * _Optional recitation_: Use `merge` and `merge_map` algorithms from Lecture Notebook to study performance of alternative strategies.  Use `%%time` and SQLite to study performance of database indices.

5. [Building machine learning models](opends4all-resources/opends4all-machine-learning)
    * **Overview and Unsupervised Models**, 1 lecture hour, basic.
    * **Supervised Models, Decision Trees, Random Forests**, 1-1.5 lecture hours, basic.
    * **Linear and Logistic Regression**, 1-1.5 lecture hours, basic.
    * **Neural Networks**, builds upon linear and logistic regression, 2-4 lecture hours, intermediate [requires understanding of calculus].

6. [Validating and tuning models](opends4all-resources/opends4all-model-assessment), 1.5-3 hours, basic

Additional and advanced topics:

* [Data ethics](opends4all-resources/opends4all-ethics), 1-2 hours, basic, most appropriately covered after a discussion of machine learning models.

* [Data exploration and visualization](opends4all-resources/opends4all-exploratory-data-analysis), 1-2 hours, basic.

* [Big data and the cloud](opends4all-resources/opends4all-scalable-data-processing), 3-5 hours, intermediate.  Most appropriate after a discussion of performance.
