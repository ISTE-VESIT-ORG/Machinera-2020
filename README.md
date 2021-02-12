
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
* Data Preprocessing
  * [scikit-learn](#scikit-learn) 
  <!--
  change this/add others as needed 
  -Hridesh 
  -->

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

## Scikit-learn

Scikit-learn (Sklearn) is the most useful and robust library for machine learning in Python. It provides a selection of efficient tools for **machine learning** and **statistical modeling** including classification, regression, clustering and dimensionality reduction via a consistence interface in Python. This library, which is largely written in Python, is built upon [NumPy](https://numpy.org/doc/stable/contents.html), [SciPy](https://matplotlib.org/contents.html) and [Matplotlib](https://matplotlib.org/contents.html)

The topics covered are: 

1. Enviornment Setup (`pip install scikit-learn`)
2. Handling Missing and Duplicate Data
3. Extract Dependent and Independent variables
4. Encoding Categorical Data
5. Splitting dataset into training and test set
6. Feature scaling

_For more details, visit the [Scikit-learn ](https://devdocs.io/scikit_learn/)_
