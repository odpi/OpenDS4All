# Contribution Guidelines

## Educational Modules

The building blocks of this repository are __modules__.  Each module covers one or more lessons that can be taught at undergraduate or graduate level ( at any higher educational institution ).  

Modules should be:

- mostly independent of other modules 
- cover a limited number of topics
- the coverage of a topic should be substantial and thorough if it is not an introductory or an overview module  

The components of a module are:

- a set of PowerPoint slides ( with presenter notes )
- a Jupyter notebook
- a quiz
- a homework assignment
- instructor notes 
- additional documentation ( where applicable )

The __minimum requirement__ for a module to be considered for inclusion in this repository is that it contains:

- a set of PowerPoint slides ( with presenter notes )
  - 30 or more slides are recommended
  - there must be enough substance in the slide deck to cover at least a 50-minute lecture 
- a Jupyter notebook ( illustrating how material covered in the slides are applied to one or more data sets )
  - use public data sets that are available for download or accessible through a hyperlink   
  - do not assume dependent packages are pre-installed in the user's Jupyter environment
  - import all modules needed to run the code cells successfully 
  - keep the markdown cells as simple as possible  
    __NB!__ The Jupyter notebook my be omitted in special cases, such as in Foundational modules where no accompanying data sets exist. But, this should be the exception rather than the rule.
- a short summary of the module with a set of learning outcomes ( in a text or a markdown file )
  - 300 or less words are recommended ( for the summary )
  - use active verbs when formulating outcomes
  - make sure the the outcomes are measurable 
  - examples of learning outcomes are
    - understand sampling, probability theory, and probability distributions
    - implement descriptive and inferential statistics using Python
    - demonstrate ability to visualize data and extract insight

Read the specifications in the [NAMING-CONVENTIONS.md](NAMING-CONVENTIONS.md) file to learn home to name your modules to facilitate search. 

## General

OpenDS4All accepts any contributions made from the community at large, with the following guidelines...

- You can submit an issue to https://github.com/odpi/OpenDS4All//issues. If you have any sensitive concerns or wish to report a security issue, please email odpi-opends4all-private@lists.odpi.org instead and do not submit a public issue.
- All code contributed must be made under an [Apache 2 license](https://spdx.org/licenses/Apache-2.0.html), and any documentation and non-code will be received and made available by the Project under the [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/), following the [license and copyright guidelines of the ODPi](https://github.com/odpi/tsc/blob/master/process/contribution_guidelines.md#license-specification)
- All contributions must be accompanied by a [Developer Certification of Origin (DCO) signoff](https://github.com/odpi/tsc/blob/master/process/contribution_guidelines.md#developer-certificate-of-origin)
- Contributions must be made as a [pull request](https://github.com/odpi/OpenDS4All/pulls), and is subject to review by a [committer](https://github.com/odpi/OpenDS4All/blob/master/GOVERNANCE.md#committer) to be accepted.

If you have any questions or concerns - feel free to reach out to odpi-opends4all-dev@lists.odpi.org.
