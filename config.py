# config.py
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '12345')
    #MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://<username>:<password>@cluster0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    MONGO_URI = os.getenv('MONGO_URI',
    'mongodb+srv://narreshgudimetlaa:NtNaEbKiIxts9T2T@cluster0.jzhpq7t.mongodb.net/crud')
