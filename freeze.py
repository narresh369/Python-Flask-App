from flask_frozen import Freezer
from app import app,contactus_collection  # Replace with your Flask app
from flask import url_for  # Import url_for

freezer = Freezer(app)

@freezer.register_generator
def url_generator():
    yield url_for('index')
    yield url_for('contactus', _external=False)
    yield url_for('crud', _external=False)

    # Generate URLs for each contact for edit and delete pages
    for contact in contactus_collection.find():
        contact_id = str(contact['_id'])
        yield url_for('edit_contact', contact_id=contact_id, _external=False)
        yield url_for('delete_contact', contact_id=contact_id, _external=False)


if __name__ == '__main__':
    freezer.freeze()
