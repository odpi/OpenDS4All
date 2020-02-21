<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# OpenDS4All Community Guide

This project welcomes contributors from any organization or individual, provided they are
willing to follow the simple processes outlined below, as well as adhere to the 
[Code of Conduct](https://github.com/odpi/specs/wiki/ODPi-Code-of-Conduct).

## Steps to contribute

Are you new to GitHub? View this short video [What is GitHub](https://www.youtube.com/watch?v=w3jLJU7DT5E&t=0s) to gain a high-level understanding of what GitHub is and how it works. This repository uses the __fork and pull__ model ( illustrated in the video ) to manage the incorporation of new modules into the repository. 

The steps to get a module included in this repository are:
1. Review the [Contribution  Guidelines](CONTRIBUTING.md)  
1. [Open an issue](#Opening-an-issue) to cover the module you will submit to this repository ( you may need to create an account on GitHub first )
1. [Fork](#Fork-your-own-copy) the odpi / OpenDS4All repository to your own account
1. [Upload](#Uploading-your-files) and commit your files
1. [Open a pull request](#Creating-a-pull-request) to initiate a review of the uploaded module and add your Developer Certificate of Origin ( see [Why the DCO?](#why-the-dco) )
1. Wait for a committer to [review](#Responding-to-a-review) and approve the commit
1. If your module is approved, it will be merged into the main branch of the repository

### Opening an issue

Before you submit a module for possibe incorporation into this repository, open an issue to alert the committers 
( also called maintainers ) that a module may be forthcoming. The following information will assist the committers in considering your submission:

 - give the issue a descriptive title ( reflecting the subject matter in the module you would like to add )
 - briefly describe the module 
 - this step __only__ notifies the committers that you are preparing a module for possible incorporation into the repository and __does__ __not__ incorporate your module into the repository 
 - complete steps 3 through 5 ( and possibly step 6 as well ) to submit your files 
 
 ```
 2.1 Navigate to the odpi / OpenDS4All GitHub page
 2.2 Navigate to the Issues tab
 2.3 Click New issue
 2.4 In the Title field, enter a name for this issue
 2.5 Enter a short description of your module in the issue field
 2.6 Click Submit new issue
 ```

### Fork your own copy

If you are intending to contribute modules rather than browse, the easiest way to prepare a contribution is to start off by creating a fork of the OpenDS4All repository. This can be done by navigating to the OpenDS4All repository above, and logging into the GitHub UI with a registered account. You will then see a 'Fork' button at the top right, and should click this to create your own fork to work with OpenDS4All.

```
3.1 Click the Fork button in the top right
```

### Uploading your files

You are now ready to upload your module's files to the branch created in the previous step.    

```
4.1 Click the opends4all-resources folder to drill down to the various categories
4.2 Select the category where you would like your module to be hosted
4.3 Click Upload files
4.4 Click choose your files
4.5 Select your files ( and press "Open" or "Enter" if required )
4.6 Click Commit changes
```

### Creating a pull request

The easiest way to create a pull request is by selecting your working branch, and clicking on 'New pull request'. Add your Developer Certificate of Origin and submit your request to the OpenDS4All committers for review and inclusion in the repository.

```
5.1 On the code tab, click New pull request
5.2 Click Create pull request
5.3 Enter the same title you used when you opened an issue ( in step 2 )
5.4 Add the short desciption of the module to the text box below the title
5.5 Add your DCO below the short description 
5.6 Click Create pull request
```

It is now up to the committers to review your contribution and make a decision whether the module will be incorporated into the repository or not.  

### Responding to a review

If your submission is rejected or needs modifying, the committers may respond with comments and suggestions in a review of the pull request. 

```
6.1 Navigate to the odpi / OpenDS4All GitHub page
6.2 Navigate to the Pull requests tab
6.3 Click the Pull request you issued
6.4 Read the comments and Leave a comment if required
6.5 Click Comment
```

### Additional tips

If you are new to GitHub, prepare your PowerPoint slide decks, Jupyter notebooks and other documentation __outside__ of GitHub. When you are ready to submit your module, save your files in a folder that is easily accessible from your computer and only then use GitHub to __upload__ and __submit__ your module for review and possible incorporation into the OpenDS4All repository. 

### Why the DCO?

We have tried to make it as easy as possible to make contributions. 
This applies to how we handle the legal aspects of contribution.

We simply ask that when submitting a module for review,
the developer must include a sign-off statement in the commit message.
This is the same approach that the
[Linux® Kernel community](http://elinux.org/Developer_Certificate_Of_Origin)
uses to manage code contributions.

Here is an example Signed-off-by line, which indicates that the submitter accepts the DCO:

```
Signed-off-by: John Doe <john.doe@hisdomain.com>
```

By signing your work, you are confirming that the origin of the content
makes it suitable to add to this project.  See
[Developer Certificate of Origin (DCO)](https://developercertificate.org/).

----
License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/),
Copyright Contributors to the ODPi Egeria project.
