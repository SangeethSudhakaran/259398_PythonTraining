from pymongo import MongoClient
import pandas as pd

connection_string = "mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
try:  
    client = MongoClient (connection_string, tlsAllowInvalidCertificates=True)
    print("connected to mongo atlas success")
    db = client['ust_live_quiz']
    collection = db['basic_collection_test']

    # 673465296f4098a5b8d9d059
    sample_data = {
        "name":"Sangeeth Sudhakaran",
        "uid":"259398",
        "city":"Thrissur"
        }
    
    print("inserted")
    collection.insert_one(sample_data)
except Exception as e:
    print(e)




