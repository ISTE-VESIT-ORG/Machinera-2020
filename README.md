
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
  * [BeautifulSoup](#beautifulsoup)
  * [Selenium](#selenium)
  * [Scrapy](#scrapy)
* Data Preprocessing
  * [scikit-learn](#scikitlearn) 
  <!--
  change this/add others as needed 
  -Hridesh 
  -->
  * 
  
<h2>Beautiful Soup</h2>

Beautiful Soup is a pure Python library for extracting structured data from a website. It allows you to parse data from HTML and XML files. It acts as a helper module and interacts with HTML in a similar and better way as to how you would interact with a web page using other available developer tools.

Environment setup : (`pip3 install beautifulsoup4`)

Dependencies: `requests`, `parser` like `lxml` & `html5lib`

_For more details, visit the [BeautifulSoup documentation] (https://www.crummy.com/software/BeautifulSoup/bs4/doc/#)_

## Selenium

Selenium is an automation testing framework for web applications/websites which can also control the browser to navigate the website just like a human. Selenium uses a web-driver package that can take control of the browser and mimic user-oriented actions to trigger desired events. 

Environment setup : (`pip install selenium`)

_For more details, visit the [Selenium documentation] (https://scikit-learn.org/stable/getting_started.html)_

## Scrapy

Scrapy is a high-level web crawling and web scraping framework written entirely in Python. It was designed to deploy spiders which extract structured data from webpages. Scrapy has applications in the fields of data mining, monitoring and automated testing. Being built on Twisted - an asynchronus network framework, Scrapy allows its crawlers to make simultaneous requests which makes it massively more efficient than BeautifulSoup and Selenium.
Scrapy supports both CSS and Xpath selectors like Selenium. However, it lacks native Javascript support, using Splash library to handle the job. Scrapy can easily handle multiple webpages, infinite scrolling and spoofing request headers. Further, Scrapy can also be used alongside BeautifulSoup for web scraping purposes.
The topics covered are:
1. Environment setup (Using `conda install -c conda-forge scrapy` through Anaconda)
2. Building Spiders
3. Configuring Pipelines
4. Configuring Middleware
5. Deploying Spiders

_For more details, visit the [Scrapy documentation] (https://docs.scrapy.org/en/latest/)_
