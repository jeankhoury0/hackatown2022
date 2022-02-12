import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = True
MONGO_DB_PASS= os.environ.get("MONGO_DB_PASS")
MONGODB_SETTINGS = {'host': "mongodb+srv://admin:"+MONGO_DB_PASS+"@cluster0.sjtue.mongodb.net/db1?retryWrites=true&w=majority"}
