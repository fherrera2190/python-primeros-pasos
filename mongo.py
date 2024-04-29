from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://ferbeoulve:root1234@cluster0.s9kw73z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# uri = "mongodb+srv://ferbeoulve:root1234@cluster0.s9kw73z.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    a=client.admin.command('ping')
    #client.command('ping')
    print(a)

    #print(client.list_database_names())
    collection = client["ecommerce"]["products"]
    print(collection)
    client.close()
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)