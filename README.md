
<p align="center">
  <h3 align="center">MACHINERA</h3>

  <p align="center">
    This is an AI Series where we will cover Machine Learning and Deep Learning topics from the very basics.
    All the material and codes of this series are in there respective branches.
    <br />
    <a href="https://github.com/ISTE-VESIT-ORG/Machinera-2020">View Demo</a>
    ·
    <a href="https://github.com/ISTE-VESIT-ORG/Machinera-2020/issues">Report Bug</a>
    ·
    <a href="https://github.com/ISTE-VESIT-ORG/Machinera-2020/issues">Request Feature</a>
  </p>
</p>

## Overview

We cover the following topics in the workshop 
* Web Scraping
  * [XPath and CSS-Selectors](#xpath-and-css_selectors)
  * [BeautifulSoup](#beautifulsoup)
  * [Selenium](#selenium)
  * [Scrapy](#scrapy)
* Exploratory Data Analysis
  * [Description of data](#description-of-data)
  * [Handling of data](#handling-of-duplicate-data)
     * [Duplicate data](#handling-of-duplicate-data)
     * [Missing values](#handling-of-missing-values)
  * [Handling outliers](#handling-outliers)
  * [Visualization](#visualization)
* Data Preprocessing
  * [Handling duplicate and missing data](#handling-duplicate-and-missing-data)
  * [Extract Dependent and Independent variables](#extract-dependent-and-independent-variables)
  * [Encoding Categorical Data](#encoding-categorical-data)
  * [Splitting dataset into training and test set](#splitting-dataset-into-training-and-test-set)
  * [Feature Scaling](#feature-scaling)

## XPath and CSS_Selectors

1. ***XPath***
   - Extensible Markup Language [_XML_](https://www.tutorialspoint.com/xml/xml_documents.htm#:~:text=An%20XML%20document%20is%20a,structure%20or%20a%20mathematical%20equation.) is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable
   - XPath stands for XML Path Language. It uses a non-XML syntax to provide a flexible way of addressing (pointing to) different parts of an XML document
2. ***CSS Selector***
   - A CSS selector is the first part of a CSS Rule. It is a pattern of elements and other terms that tell the browser which HTML elements should be selected to have the CSS property values inside the rule applied to them

_For more details, visit the [XPath documentation](https://developer.mozilla.org/en-US/docs/Web/XPath)_ , _[CSS Selectors Documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)_

## BeautifulSoup

Beautiful Soup is a pure ***Python*** library for extracting structured data from a website. It allows you to parse data from HTML and XML files. It acts as a helper module and interacts with HTML in a similar and better way as to how you would interact with a web page using other available developer tools

The topics covered are:

1. Environment setup : (`pip3 install beautifulsoup4`)
2. Dependencies: 
   - [`requests`](https://requests.readthedocs.io/en/master/): The Requests module lets you integrate your Python programs with web services
   - Beautiful soup works with **parser** to provide idiomatic ways of navigating, searching, and modifying the parse tree
      - HTML parser is used which serves as the basis for parsing text files formatted in HTML and XHTML, For more details, visit _[HTML.parser documentaion](https://docs.python.org/3/library/html.parser.html)_
3. Using `requests` to get all contents of website
4. Using parser to scrape the **required information**

_For more details, visit the [BeautifulSoup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#)_

## Selenium

Selenium is an automation testing framework for web applications/websites which can also control the browser to navigate the website just like a human. Selenium uses a **web-driver** package that can take control of the browser and <ins>mimic</ins> user-oriented actions to trigger desired events

The topics covered are:

1. Environment setup : (`pip install selenium`)
2. ChromeDriver - WebDriver for chrome 
   - _[WebDriver](https://www.selenium.dev/documentation/en/webdriver/)_ is an open source tool for automated testing of webapps, it provides capabilities for navigating to web pages, user input, JavaScript execution, and more.
   - _To download ChromeDriver, visit [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads)_
3. Selenium scraper
   - Import (`which`) from [_(`shutil`)_](https://docs.python.org/3/library/shutil.html) package
   - Launch Chrome with Selenium
   - Navigate to and from websites
   - Find Element by _[ID ](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id)_/_[ Tag ](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)_/_[ Class_Name ](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/class)_/_[ Xpath ](https://developer.mozilla.org/en-US/docs/Web/XPath)_/_[ CSS_Selector ](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)_
   - Display the scraped content
4. WhatsApp spam messages
   - Use selenium to send ***Automated messages***

_For more details, visit the [Selenium documentation](https://www.selenium.dev/documentation/en/)_

## Scrapy

Scrapy is a high-level web crawling and web scraping framework written entirely in ***Python***. It was designed to deploy [(`spiders`)](https://docs.scrapy.org/en/latest/topics/spiders.html) which extract structured data from webpages. Scrapy has <ins>applications</ins> in the fields of **data mining**, **monitoring** and **automated testing**. Being built on _[Twisted](https://docs.twistedmatrix.com/en/twisted-18.9.0/)_ - an asynchronus network framework, Scrapy allows its crawlers to make simultaneous requests which makes it massively more efficient than <ins>BeautifulSoup</ins> and <ins>Selenium</ins>

Scrapy supports both CSS and Xpath selectors like Selenium. However, it lacks native Javascript support, using _[Splash library](https://splash.readthedocs.io/en/stable/)_ to handle the job. Scrapy can easily handle **multiple webpages**, **infinite scrolling** and **spoofing request headers**. Further, Scrapy can also be used alongside BeautifulSoup for parsing web pages.

The topics covered are:

1. Environment setup (Recommended through Anaconda using `conda install -c conda-forge scrapy`)
2. Building Spiders
3. Configuring Pipelines
4. Configuring Middleware
5. Deploying Spiders

Dependencies include: [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#), [parsel](https://pypi.org/project/parsel/), [w3lib](https://pypi.org/project/w3lib/), [Twisted](https://twistedmatrix.com/trac/) and [pyOpenSSL](https://pypi.org/project/pyOpenSSL/)

_For more details, visit the [Scrapy documentation](https://docs.scrapy.org/en/latest/)_

## Exploratory Data Analysis

## Description of data

_[Pandas](https://pandas.pydata.org/docs/)_ provide various functions/attributes which give us detailed insight of our dataset. some of them are

* `df.head(n)` - returns first n values
* `df.tail(n)` - returns last n values
* `df.shape`   - returns shape of the dataframe
* `df.dtypes`  - returns datatype of each attribute(column) of the dataset
* `df.info()`  - returns the count of Non-null values present in each column
* `df.describe()` - returns basic statistical info about dataset

_For more details of these functions, visit [API reference of Pandas documentation](https://pandas.pydata.org/docs/reference/index.html)_

## Handling of duplicate data

   * Duplicate records could make our model *biased* and thus are unwanted. We can remove duplicate values by using `drop_duplicate()` function.

## Handling of missing values

   * If there are *missing values* in a numerical data feature then mathematical operations will fail. If they are present in categorical data feature then during label encoding they might become a separate category. Thus it is necessary to remove these values.
   * We have `dropna()` function which removes these values for us

_For more details, visit [Handling missing values in Pandas](https://www.youtube.com/watch?v=fCMrO_VzeL8), [Dealing with missing data](https://towardsdatascience.com/dealing-with-missing-data-in-data-science-projects-e8ac7a4efdff)_

## Handling Outliers

   * Outliers are the values which are significantly different from other *values/observations*. An outlier can create major issues in *modelling*. So it is necessary to find outliers and treat them.
   * Outliers can be detected by using [***Boxplot***](https://seaborn.pydata.org/generated/seaborn.boxplot.html). Boxplot depicts the variable distribution using quartile. It is also known as a *box* and *whiskers* plot.

_For more details, visit [Dealing with outliers](https://cxl.com/blog/outliers/)_

## Visualization

We will be using ***Sweetviz*** for visualization. Sweetviz is an open-source Python library that generates beautiful, high-density visualizations to help with **Exploratory Data Analysis (EDA)**. The output obtained from this library is a fully self-contained HTML application. The system is built with a focus on **target value visualisation** and **comparision of datasets** in an efficient, rapid fashion. The goal of the Sweetviz project is to help quick analysis of target characteristics, training vs testing data, and other such data characterization tasks. The Sweetviz library is under active development and has been constantly working to improve performance and eliminate bugs.

The topics covered are: 

1. Enviornment Setup (`pip install sweetviz`)
2. EDA using Sweetviz
3. Visualisation of Data

_For more details, visit the [Sweetviz Documentation](https://pypi.org/project/sweetviz/), [Alternatives to Sweetviz](https://analyticsindiamag.com/tips-for-automating-eda-using-pandas-profiling-sweetviz-and-autoviz-in-python/#:~:text=Sweetviz%20is%20a%20python%20library,we%20used%20for%20pandas%20profiling.)_


## Data Preprocessing

## Handling duplicate and missing data

Duplicate records could make our model biased and thus are unwanted. We have used `drop_duplicate()` function to remove duplicate values.

If there are missing values in a numerical data feature then mathematical operations will fail (i.e. throw an error). If they are present in categorical data feature then during label encoding they might become a separate category. Thus it is necessary to remove these values.
We have used `dropna()` function to remove these values for us.


## Extract Dependent and Independent variables

Independent variables (also referred to as Features) are the input for a process that is being analyzes. Dependent variables are the output of the process.
For example, in the below data set, the independent variables are the input of the purchasing process being analyzed. The result (whether a user purchased or not) is the dependent variable.

_Reference: [Splitting data in dependent and independent variables](https://www.pluralsight.com/guides/importing-and-splitting-data-into-dependent-and-independent-features-for-ml)_

## Encoding Categorical Data

1. **Label Encoding:**
When we give our Dataset to model we need to have all numerical data into it, this implies that we have to eliminate all the string type data. This is achieved by Label encoding.
In label encoding all the categories are enlisted in a numpy array and the index of that array is used to replace all the categories in that column. 
`preprocessing.LabelEncoder()` of sklearn is used for label encoding

2. **One Hot Encoding:**
The main drawback of Label encoder is that it introduces hierarchy in the categorical data which is unwanted most of the times. To overcome this drawback one hot encoding is used.
What one hot encoding does is, it takes a column which has categorical data, which has been label encoded, and then splits the column into multiple columns. The numbers are replaced by 1s and 0s, depending on which column has what value.

_Further reading -_
  * _[Feature Engineering](https://www.youtube.com/watch?v=6WDFfaYtN6s)_
  * _[Encoding Data](https://www.analyticsvidhya.com/blog/2020/08/types-of-categorical-data-encoding/)_

## Splitting dataset into training and test set

We use train-test-split module from sklearn to divide our dataset in training and testing parts. By doing this we allow our model to learn from larger chunk of data and then we can test its accuracy using smaller chunk of data.

We Import train-test-split by following command -
`from sklearn.model_selection import train_test_split`

When splitting a dataset there are some competing concerns:
* If you have less training data, your parameter estimates have greater variance.
* And if you have less testing data, your performance statistic will have greater variance.
* The data should be divided in such a way that neither of them is too high, which is more dependent on the amount of data you have.
* If your data is too small then no split will give you satisfactory variance so you will have to do cross-validation.
* If your data is huge then it doesn’t really matter whether you choose an 80:20 split or a 90:10 split


## Feature Scaling

Feature scaling refers to putting the values in the same range or same scale so that no variable is dominated by the other.
Numerical data in the dataset can have varied range i.e. one parameter may lie between 1 to 10 for all records whereas another parameter can lie between 1000 to 5000. Though data is logically correct but after passing to particular algorithm, the features with higher magnitude become key parameters for that algorithm.

To avoid such situations feature scaling is performed using some statistical techniques like Min-Max scaling & Mean normalization. This creates a common range for all the parameters and thus removes Algorithmic bias.

_References -_
  * _[Standardization and Normalization](https://www.analyticsvidhya.com/blog/2020/04/feature-scaling-machine-learning-normalization-standardization/)_
  * _[Difference between Standardization and Normalization](https://www.youtube.com/watch?v=mnKm3YP56PY)_
