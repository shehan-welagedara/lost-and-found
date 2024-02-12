from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import engine
from sqlalchemy import text
import base64
from flask import request

app = Flask(__name__)


def load_lost_items():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM `lost_items`"))
        columns = result.keys()

        result_lost = []
        for row in result.fetchall():
            result_lost.append(dict(zip(columns, row)))
        return result_lost
    
def load_found_items():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM `found_items`"))
        columns = result.keys()

        result_found = []
        for row in result.fetchall():
            result_found.append(dict(zip(columns, row)))
        return result_found

def insert_lost_item(name, location, date, description, contact, photo):
    with engine.connect() as conn:
        query = text("INSERT INTO lost_items (name, location, date, description, contact_number, photo) VALUES (:name, :location, :date, :description, :contact, :photo)")
        conn.execute(query, {"name": name, "location": location, "date": date, "description": description, "contact": contact, "photo": photo})
        conn.commit()

def insert_found_item(name, location, date, description, contact, photo):
    with engine.connect() as conn:
        query = text("INSERT INTO found_items (name, location, date, description, contact_number, photo) VALUES (:name, :location, :date, :description, :contact, :photo)")
        conn.execute(query, {"name": name, "location": location, "date": date, "description": description, "contact": contact, "photo": photo})
        conn.commit()

def load_latest_lost_items():
    with engine.connect() as conn:
        query = text("SELECT * FROM lost_items ORDER BY date DESC LIMIT 10")
        result = conn.execute(query)
        columns = result.keys()
        lost_items = [dict(zip(columns, row)) for row in result.fetchall()]
        return lost_items

def load_latest_found_items():
    with engine.connect() as conn:
        query = text("SELECT * FROM found_items ORDER BY date DESC LIMIT 10")
        result = conn.execute(query)
        columns = result.keys()
        found_items = [dict(zip(columns, row)) for row in result.fetchall()]
        return found_items

@app.route('/')
def index():
    latest_lost_items = load_latest_lost_items()
    latest_found_items = load_latest_found_items()
    return render_template('index.html', latest_lost_items=latest_lost_items, latest_found_items=latest_found_items)

@app.route('/item/lost/<int:item_id>')
def view_lost_item(item_id):
    with engine.connect() as conn:
        query = text("SELECT * FROM lost_items WHERE id = :item_id")
        result = conn.execute(query, {"item_id": item_id})
        columns = result.keys()
        item_details = dict(zip(columns, result.fetchone()))
        return render_template('item_details.html', item_details=item_details)

@app.route('/item/found/<int:item_id>')
def view_found_item(item_id):
    with engine.connect() as conn:
        query = text("SELECT * FROM found_items WHERE id = :item_id")
        result = conn.execute(query, {"item_id": item_id})
        columns = result.keys()
        item_details = dict(zip(columns, result.fetchone()))
        return render_template('item_details.html', item_details=item_details)

@app.template_filter('b64encode')
def b64encode_filter(data):
    if data:
        return base64.b64encode(data).decode('utf-8')
    else:
        return None

@app.route('/report_lost', methods=['GET', 'POST'])
def report_lost():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        date = request.form['date']
        description = request.form['description']
        contact = request.form['contact']
        
        if 'itemPhoto' in request.files:
            photo = request.files['itemPhoto'].read()
        else:
            photo = None
        
        insert_lost_item(name, location, date, description, contact, photo)

        return redirect(url_for('index'))

    return render_template('report_lost.html')

@app.route('/report_found', methods=['GET', 'POST'])
def report_found():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        date = request.form['date']
        description = request.form['description']
        contact = request.form['contact']
        photo = request.files['itemPhoto'].read()

        insert_found_item(name, location, date, description, contact, photo)

        return redirect(url_for('index'))

    return render_template('report_found.html')

if __name__ == '__main__':
    app.run(debug=True)
