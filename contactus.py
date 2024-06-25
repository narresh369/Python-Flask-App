# contactus.py
from pymongo import MongoClient
from config import Config

# Connect to MongoDB using the URI from the config
client = MongoClient(Config.MONGO_URI)

# Access the database (you can specify the database name you want to use)
db = client.get_database()

# Create or access the 'contactus' collection
contactus_collection = db['contactus']

def get_contact_info():
    return contactus_collection.find()

def get_contact_count():
    return contactus_collection.count_documents({})

# Function to insert a contact us message
def insert_contactus_message(name, email, mobile, message):
    contactus_document = {
        'name': name,
        'email': email,
        'mobile': mobile,
        'message': message
    }
    result = contactus_collection.insert_one(contactus_document)
    return result.inserted_id
# Sample data
# The `dataContactus` variable is storing a list of dictionaries, where each dictionary represents
# information about different office locations. Each dictionary contains keys such as "office",
# "address", "city", and "mobile" with corresponding values providing details about the office
# location, address, city, and contact mobile number. This data could potentially be used for
# displaying office contact information or for any other relevant purposes within the application.
# `dataContactus` seems to be a list of dictionaries containing information about different office
# locations. Each dictionary represents a different office location and includes details such as the
# office name, address, city, and mobile contact number. This data could potentially be used for
# displaying office contact information on a website or for other purposes related to managing contact
# details for different branches or locations.
dataContactus = [
    {"office": "Main Branch", "address": "1-119-3, Adarsh Nagar,MVP Colony", "city":"Visakhapatnam", "mobile": "+91 9949570732"},
    {"office": "Server Location", "address": "1-63,Highway Bypass, Yendada", "city":"Visakhapatnam", "mobile": "+91 9963258741"},
    {"office": "Management Building", "address": "1-44-3, LB Colony,MVP", "city":"Visakhapatnam", "mobile": "+91 9987456321"},
    {"office": "IT Branch", "address": "1-18/3,2nd Circle,MVP", "city":"Visakhapatnam", "mobile": "+91 9911345678"},
]