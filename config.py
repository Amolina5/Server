import pymongo
import certifi

# this is the connection string that i got from the mongodb connection
con_string = "mongodb+srv://test:test@cluster0.vqy5z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongodbClient(con_string, tlsCAFile = certifi.where())