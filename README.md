---
page_type: sample
languages:
- python
products:
- AWS DocumentDB 
description: "This sample demonstrates a Python application that will be make a 360 view for the enduser "

---
# Develop a 360 view application in python with Amazon DocumentDB and cloud 9

## About this sample

> This sample is based on a real client need how to consolidate different source in one collections

### Overview

This sample demonstrates a Python application that will generate a consolidated view 

1. a script that will use mongo command to load data in collections from csv and json 
2. an application that will consolidate 3 collection in one.



## How to run this sample

To run this sample, you'll need:

> - [Python 2.7+](https://www.python.org/downloads/release/python-2713/) or [Python 3+](https://www.python.org/downloads/release/python-364/)

> - An AWS DocumentDB cluster and A cloud 9 to interact with the documentdb , if you don't know how to do this you can use the tuttorial at the following address https://aws.amazon.com/fr/getting-started/hands-on/getting-started-amazon-documentdb-with-aws-cloud9/


### Step 1:  Clone or download this repository

From your shell or command line in cloud 9 :

```Shell
git clone https://github.com/emmanueldeletang/306view-in-documentdb-
```

or download and extract the repository .zip file.

> Given that the name of the sample is quite long, you might want to clone it in a folder close to the root of your hard drive, to avoid file name length limitations when running on Windows.

### Step 2:  install the pre-requisite python library 

cd the folder where you have install the file 

- You will need to install dependencies using pip as follows:
```Shell
$ python -m pip install pymongo 


```

change the db name , the key and endpoint of your cosmosdb . 
### Step 3:  Run the application  

Run the generator to generate data in c1, C2,C3  collections and the conso collection will be create , after launch the sampleconso.py that make the consolidation 

in the import.sh replace 

MYCLUSTER.docdb.amazonaws.com:27017 by your cluster endpoint 
adjust the pem folder if need ../rds-combined-ca-bundle.pem
replace  USER by your documentdb username and XXXX by your Documentdb password

launch the import by command and intialize the global information in the shell 
```Shell
$source ./import.sh

$export clusterendpoint=yourdocumentdb .docdb.amazonaws.com:27017
$export password=.....
$export username=.... 
```
The import will create 3 collections C1, C2 , C3 in the database vue in your documentdb 


```Shell


$ python conso2.py

```
The python will create a new collection clients , with the aggregation of all the data in C 1 , C2 , C3 based on customer 

you can check using mongo shell .... 


in addition a word with more information will arrive in the future 

