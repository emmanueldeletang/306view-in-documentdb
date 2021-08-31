#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import os
import sys
import pymongo
import copy


#Get Amazon DocumentDB ceredentials from enviornment variables
username = os.environ.get("username")
password = os.environ.get("password")
clusterendpoint = os.environ.get("clusterendpoint")

mongo =  pymongo.MongoClient(clusterendpoint, username=username, password=password, ssl='true', ssl_ca_certs='rds-combined-ca-bundle.pem',retryWrites='false')
db = mongo.vue



clients = db.clients
c1 = db.c1
c2 = db.c2
c3 = db.c3

db.clients.drop()


print("load  od  c1 --> clients")

for doc in c1.find():
    c1 = copy.copy(doc)
    del c1["_id"]
    doc["c1"] = c1
    clients.insert_one(doc)


print("load of c2 --> clients (pivot = email)")

for doc in c2.find():
    del doc["_id"]
    clients.update_one({"email":doc["email"]},
        {"$set":{"medicaments":doc["medicaments"],
                 "c2":doc}})



print("load of C3  (tel et adresses) --> clients (pivot = nom et prenom)")

for doc in c3.find():
    del doc["_id"]
    clients.update_one({"nom":doc["nom"],"prenom":doc["prenom"]},
        {"$addToSet":{"adresse":{"$each":doc["adresse"]}},
         "$set":{"c3":doc}})


print("delete of sub document C1 and C2 for exemple ")

for doc in clients.find():
    c1 = copy.copy(doc)
    del doc["c2"]
    del doc["c1"]
    clients.replace_one(c1,doc)


    
    

