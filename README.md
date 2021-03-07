
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
* [What is Machine Learning?](#what-is-machine-learning)
* [Types of Machine Learning](#types-of-machine-learning)
  * [Supervised Learning](#Supervised-learning)
  * [Unsupervised Learning](#Unsupervised-learning)
  * [Reinforcement Learning](#Reinforcement-learning)
* [Algorithms Covered](#algorithms-covered)
  * Supervised Learning
    * [Regression](#Regression)
    * [Classification](#Classification)
  * Unsupervised Learning
    * [Clustering](#Clustering)
 
## What is Machine Learning?

Machine learning is an branch of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it to learn for themselves.

_For more details, check out [Fundamentals of Machine learning](https://www.ibm.com/cloud/learn/machine-learning)._

## Types of Machine Learning

Largely, there are three major recognized categories of Machine Learning: supervised learning, unsupervised learning and reinforcement learning. This course will review the implimentation of supervised and unsupervised learning.

_For more details, check out [Machine Learning Types](https://towardsdatascience.com/what-are-the-types-of-machine-learning-e2b9e5d1756f)._
### Supervised Learning

Supervised learning is often described as a ***task-oriented form*** of Machine Learning. It is highly focused on a singular task, feeding more and more examples to the algorithm until it can ***accurately perform*** on that task.

<p align="center">
  <img src="https://user-images.githubusercontent.com/72266160/109978581-091b2280-7d24-11eb-8b2b-9e8c3456637f.png">
</p>

_For more details, check out the [Supervised Learning Documentation](https://scikit-learn.org/stable/supervised_learning.html)_

### Unsupervised Learning

Unsupervised learning is very much the opposite of supervised learning. It features ***no labels***. Instead, our algorithm would be fed a lot of data and given the tools to understand the ***properties of the data***. 

<p align="center">
  <img src="https://user-images.githubusercontent.com/72266160/109978594-0ddfd680-7d24-11eb-87c0-2dd904e563f5.png">
</p>

_For more details, check out the [Unsupervised Learning Documentation](https://scikit-learn.org/stable/unsupervised_learning.html)_

### Reinforcement Learning

Reinforcement learning is fairly different when compared to supervised and unsupervised learning. Reinforcement learning is concerned with how intelligent agents ought to take actions in an environment in order to maximize the ***notion of cumulative reward***. In case the model makes bad decisions, the behaviour is ***corrected through penalties***.

<p align="center">
  <img src="https://user-images.githubusercontent.com/72266160/109980279-ba6e8800-7d25-11eb-9cbf-76eb8e292f4e.png">
</p>

_For more details, check out the [Reinforcement Learning Documentation](https://towardsdatascience.com/reinforcement-learning-tutorial-part-1-q-learning-cadb36998b28)_

## Algorithms We Covered 

### Regression

Regression analysis consists of a set of machine learning methods that allow us to predict a ***continuous outcome variable (y)*** based on the value of one or multiple ***predictor variables (x)***. Briefly, the goal of regression model is to build a mathematical equation that defines y as a function of the x variables. The course shows the implementation of:

* [Linear Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
* [Polynomial Regression](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)
* [Decision Tree Regression](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html)
* [Random Forest Regression](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
* [Support Vector Regression](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html).

### Classification

In machine learning, classification refers to a predictive modeling problem where a ***class label*** is predicted for a ***given example of input data***. Given one or more inputs a classification model will try to predict the value of one or more outcomes. Outcomes are labels that can be applied to a dataset. The course shows the implementation of:
* [K-Nearest Neighbour Classification](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
* [Decision Tree Classification](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
* [Random Forest Classification](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
* [Support Vector Classification](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
* [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
* [Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html)

### Clustering
Cluster analysis, or clustering, is an unsupervised machine learning task. It involves automatically discovering ***natural grouping in data***. Unlike supervised learning (like predictive modeling), clustering algorithms only interpret the input data and find natural groups or clusters in feature space. The course shows the implimentation of ***_[K-Mean Clustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)._***

