from flask import Flask, render_template, request, redirect, url_for
from database import engine
from sqlalchemy import text
from database import load_latest_items

app = Flask(__name__)

def load_lost_items():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM `lost_items`"))
        # Get column names
        columns = result.keys()

        result_lost = []
        for row in result.fetchall():
            result_lost.append(dict(zip(columns, row)))
        return result_lost
    
def load_found_items():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM `found_items`"))
        # Get column names
        columns = result.keys()

        result_found = []
        for row in result.fetchall():
            result_found.append(dict(zip(columns, row)))
        return result_found

def load_lost_and_found():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM `lost_and_found`"))
        # Get column names
        columns = result.keys()

        result_items = []
        for row in result.fetchall():
            result_items.append(dict(zip(columns, row)))
        return result_items

def insert_lost_item(name, location, date, description, contact, photo):
    with engine.connect() as conn:
        query = text("INSERT INTO lost_items (name, location, date, description, contact_number, photo) VALUES (:name, :location, :date, :description, :contact, :photo)")
        conn.execute(query, {"name": name, "location": location, "date": date, "description": description, "contact": contact, "photo": photo})
        conn.commit()  # Commit the transaction

# Define function to insert data into found_items table
def insert_found_item(name, location, date, description, contact, photo):
    with engine.connect() as conn:
        query = text("INSERT INTO found_items (name, location, date, description, contact_number, photo) VALUES (:name, :location, :date, :description, :contact, :photo)")
        conn.execute(query, {"name": name, "location": location, "date": date, "description": description, "contact": contact, "photo": photo})
        conn.commit()  # Commit the transaction

@app.route('/')
def index():
    latest_items = load_latest_items()
    return render_template('index.html', latest_items=latest_items)

from flask import request

@app.route('/report_lost', methods=['GET', 'POST'])
def report_lost():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        date = request.form['date']
        description = request.form['description']
        contact = request.form['contact']
        
        # Check if the 'itemPhoto' field exists in the request.files
        if 'itemPhoto' in request.files:
            photo = request.files['itemPhoto'].read()
            # Process the photo data
        else:
            photo = None  # Set to None if no photo provided
        
        # Now you can insert the data into the database
        insert_lost_item(name, location, date, description, contact, photo)

        # Redirect to index page after successful submission
        return redirect(url_for('index'))

    return render_template('report_lost.html')


@app.route('/report_found', methods=['GET', 'POST'])
def report_found():
    # Handle form submission
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        location = request.form['location']
        date = request.form['date']
        description = request.form['description']
        contact = request.form['contact']
        photo = request.files['itemPhoto'].read()

        # Insert data into found_items table
        insert_found_item(name, location, date, description, contact, photo)

        # Redirect to index page
        return redirect(url_for('index'))

    return render_template('report_found.html')

@app.route('/latest_items')
def latest_items_list():
    latest_items = load_lost_and_found()  # Assuming this function returns combined data from lost and found items
    return render_template('latest_items.html', latest_items=latest_items)

@app.route('/item/<int:item_id>')
def item_details(item_id):
    # Placeholder code to retrieve item details from the database
    # For now, let's assume we have a function to fetch item details
    item = {"id": item_id, "name": "Sample Item", "date": "2024-02-10", "description": "Sample description", "status": "Lost"}
    return render_template('item_details.html', item=item)

if __name__ == '__main__':
    app.run(debug=True)
