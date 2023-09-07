# Estimating-Home-Value

# Project Discription

#### Zillow wants to be able to predict the Property Tax Assesed Values of Single Family Properties that had a transaction during 2017. We want to make improvments on the existing model by creating new features, using regression algorithms, or by creating models for each county.

#### Why are you tackling this project?

#### Why is this important?

#### our current model has been neglected and is in need of improvment. We can get better results by creating new features.

#### How could it be of use to someone else beyond just the intrest or new knowledge?

#### Once the model is created it can be used as a template to create new or better models for future problems.

# Goals
    - Construct a ML Regression model that predicts property tax assessed values of Single Family Properties using attributes of the properties

    - Find the key drivers of property value for single family properties

    - Deliver a report that the data scientest team can read through and replicate, understand what steps were taken, why and what the outcome was.

    - make recommendations on what works or doesn't work in predicting these homes' values.

# The Plan

### Aquire Zillow data from MySQL

### Prepare data
- drop null values
- rename columns
- what do I do with fips?
- split the data
- scale the data

### Explore the data for predicters of property tax value
- This will be a list of questions that lead to my findings

### Develop a regression model that accuratly predicts property tax value
- Use drivers identified in explore to build predictive models of different types Evaluate models on train and validate data Select the best model based on highest accuracy Evaluate the best model on test data Draw conclusions

# Data Dictionary

|Feature|Definition|
|-|-|
|area|useable sqft in the home|

# Steps to reporduce
- Clone this repo
- Acquire Zillow data set from MySQL
- Put the Zillow data in the same file containg the cloned repo
- Run the notebook

# Key Take aways and conclusions
- something about counties/ location
- something about year
- somthing about sqft/area

# Recommendations
- maybe talk about new ways to collect data?
- maybe run your model on homes for 2018 and see how effective it is
