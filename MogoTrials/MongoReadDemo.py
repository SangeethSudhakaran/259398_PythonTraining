from pymongo import MongoClient
import pandas as pd

connection_string = "mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient (connection_string, tlsAllowInvalidCertificates=True)
    print("connected to mongo atlas success")

    # connect tow mongo cluster sample_mflix 
    db = client['ust_live_quiz']

    # access a collection movies
    collection = db['basic_collection_test']

    #Query the collection
    results = collection.find().limit(100)
    # for doc in results:
    # print(doc)
    # break
except Exception as e:
    print(e)
finally:
    print('Hi')
    #client.close()
 #print(type (results))
result_list = list(results) # print(type (result_list)) # print(result_list[:4])
df = pd.DataFrame(result_list)
print(df) 
print(df.columns)
