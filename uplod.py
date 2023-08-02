
from pymongo.mongo_client import MongoClient
import pandas as pd
import json
import dns.resolver


## uniform resource indentfier
uri = "mongodb+srv://yash:yashrajdb@cluster0.eax8z.mongodb.net/?retryWrites=true&w=majority"

dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8'] # this is a google public dns server,  use whatever dns server you like here
# as a test, dns.resolver.query('www.google.com') should return an answer, not an exception

# Create a new client and connect to the server
client = MongoClient(uri)

# create database name and connection name
DATABASE_NAME = "Pwskills"
DATABASE_NAME = "waferfault"

# read the data as a dataframe
df = pd.read_csv(r"C:\Users\Raju\OneDrive\Desktop\sensor-fault-detection\notebooks\wafer_23012020_041211.csv")
df = df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

# now dump the data into the database
client[DATABASE_NAME][DATABASE_NAME].insert_many(json_record)

# Send a ping to confirm a successful connection
