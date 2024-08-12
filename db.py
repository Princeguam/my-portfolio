from mongoengine import *
from os import getenv
from dotenv import load_dotenv
from datetime import datetime

# DATABASE CONFIGURATION
load_dotenv()

connect('my_pfDB', host=getenv("DB_URI"))


# CREATING DB MODELS
class Contact(Document):
    email = StringField(required=True, max_length=40)
    text = StringField(required=True, max_length=50)
    message = StringField(required=True, max_length=150)
    created_at = DateTimeField(default=datetime.now)
    #
    # def to_db(self):
    #     email = self.email
    #     text= self.text
    #     message = self.message
    #     date_sent = self.created_at(datetime.now())
