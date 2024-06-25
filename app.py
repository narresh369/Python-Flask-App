from flask import Flask, render_template, request, redirect, url_for, flash
from flask_pymongo import PyMongo
from config import Config
from contactus import insert_contactus_message, get_contact_info,get_contact_count
from charts import get_chart_data
from bson.objectid import ObjectId
#======================================
from pymongo import MongoClient

# Connect to MongoDB using the URI from the config
client = MongoClient(Config.MONGO_URI)

# Access the database (you can specify the database name you want to use)
db = client.get_database()

# Create or access the 'contactus' collection
contactus_collection = db['contactus']

#======================================

app = Flask(__name__)
app.config.from_object(Config)

mongo = PyMongo(app)

@app.route('/')
def index():
    contacts = get_contact_info()
    contact_count = get_contact_count()  # Count the number of contacts
    chart_data = get_chart_data()        # Get chart data from charts.py
    return render_template('index.html', contacts=contacts,contact_count=contact_count, chart_data=chart_data)

@app.route('/contactus.html', methods=['GET', 'POST'])
def contactus():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        message = request.form.get('message')

        if not all([name, email, mobile, message]):
            flash('All fields are required!', 'danger')
        else:
            insert_contactus_message(name, email, mobile, message)
            flash('Your details have been submitted successfully!', 'success')
        return redirect(url_for('index'))

    contacts = get_contact_info()
    contact_count = get_contact_count()  # Count the number of contacts
    chart_data = get_chart_data()        # Get chart data from charts.py
    return render_template('index.html', contacts=contacts,contact_count=contact_count, chart_data=chart_data)

@app.route('/crud.html')
def crud():
    contacts = get_contact_info()
    contact_count = get_contact_count()  # Count the number of contacts
    return render_template('crud.html', contacts=contacts,contact_count=contact_count)

@app.route('/edit_contact/<contact_id>.html', methods=['GET', 'POST'])
def edit_contact(contact_id):
    # Retrieve the contact with the specified _id from MongoDB
    contact = get_contact_by_id(contact_id)

    if not contact:
        # Handle case where contact with contact_id is not found
        app.logger.error(f"Contact not found for ID: {contact_id}")
        return 'Contact not found', 404

    if request.method == 'POST':
        # Retrieve form data and update contact
        name = request.form.get('name')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        message = request.form.get('message')

        # Update the contact in MongoDB (replace with your update logic)
        update_contact(contact_id, name, email, mobile, message)

        flash('Contact updated successfully!', 'success')
        return redirect(url_for('index'))

    # Render the edit_contact.html template with the contact data
    return render_template('edit_contact.html', contact=contact)

def get_contact_by_id(contact_id):
    """Retrieve a contact document by its _id from MongoDB."""
    return contactus_collection.find_one({'_id': ObjectId(contact_id)})

def update_contact(contact_id, name, email, mobile, message):
    """Update a contact document in MongoDB."""
    result = contactus_collection.update_one(
        {'_id': ObjectId(contact_id)},
        {'$set': {'name': name, 'email': email, 'mobile': mobile, 'message': message}}
    )
    return result.modified_count  # Return number of documents modified


@app.route('/delete_contact/<contact_id>.html', methods=['GET'])
def delete_contact(contact_id):
    contactus_collection.delete_one({'_id': ObjectId(contact_id)})
    flash('Contact deleted successfully!', 'success')
    return redirect(url_for('index'))
pass

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True,host='0.0.0.0')
