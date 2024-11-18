from pymongo import MongoClient
import pandas as pd
from bson.objectid import ObjectId


connection_string=r"mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client=MongoClient(connection_string,tlsAllowInvalidCertificates=True)
    print("connected to mongo atlassuccess")

    #connect to mongo cluster

    db=client['ust_live_quiz']

    #access a collection

    collection=db["basic_collection_test"]

    docid="673465296f4098a5b8d9d059"
    query = {"_id":ObjectId(docid)}
    update={"$set":{
        "name":"Sangeeth Sudhakaran",
        "uid":"259398",
        "city":"Thrissur"
        }}
    result=collection.update_one(query,update)
    
    query1={'age':{"$gt">20}}
    results=collection.find(query1)

    if(result.matched_count>0):
        print("there was a match, document has been found")


except Exception as e:
    print(e)


result_list=list(results)

df=pd.DataFrame(result_list)
print(df.head(20))

client.close()