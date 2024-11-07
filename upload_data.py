# upload data from local machine into mongo db 

from pymongo.mongo_client import MongoClient
import pandas as pd
import json # JAVA script object notation

# url
url = "mongodb+srv://aakif:fXHmx25n&0@cluster0.qfqxm.mongodb.net/?retryWrites=true&w=majorit&appName=Cluster0"

# create a new client and connect to server
client = MongoClient(url)



# create Db name and connection name
# (u can also create a collection manually but its better this way )

# lets just create manully as this isnt working out

# Define the database and collection names
DATABASE_NAME = "SensorFaultDetection2"
COLLECTION_NAME = "waferFault2"

# added 2 coz 1 created by mistake


# as connection is success we can login easily


df = pd.read_csv("/Users/shaikyasin/Documents/AIDS/Projects/ML projects/1 sensor fault detection/notebooks/wafer_23012020_041211.csv")




df = df.drop("Unnamed: 0",axis=1)

json_record = list(json.loads(df.T.to_json()).values())


client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

# it gives error but the whole document(json is somehow inserted)

# update the constants as per video
# as out next steps involve this