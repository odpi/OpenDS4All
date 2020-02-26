# Instructor Notes: Data Wrangling and Integration

Instructors who want more depth on this topic can refer to:

* *Principles of Data Integration*, Doan, Halevy, and Ives, Morgan Kaufmann, 2012.
* [BigGorilla Data Integration and Data Preparation](https://www.biggorilla.org/)
* [McKinney](https://www.programmer-books.com/wp-content/uploads/2019/04/Python-for-Data-Analysis-2nd-Edition.pdf), Chapters 6, 7, 9

## DATASET

Our dataset is from a crawl of webpages related to wikipedia and other websites. It is stored in OpenDS4All/assets/data/scripts-autoload-data/data-wrangling. 
* To read from GitHub, you should follow the format of `${prefix}/${webpage}` where `${prefix}=https://raw.githubusercontent.com/odpi/OpenDS4All/penn-processing-zgi/assets/data/scripts-autoload-data/data-wrangling/` and `${webpage}` is the url of the actual crawled webpage, without `http(s)://`. 
* For example, if you want to visit `https://en.wikipedia.org/wiki/List_of_cryptocurrencies`, you should actually enter `https://raw.githubusercontent.com/odpi/OpenDS4All/penn-processing-zgi/assets/data/scripts-autoload-data/data-wrangling/en.wikipedia.org/wiki/List_of_cryptocurrencies`. 
