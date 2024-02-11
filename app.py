from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for testing
dummy_lost_items = [
    {"id": 1, "name": "Lost Item 1", "date": "2024-02-10", "description": "Lost item description 1"},
    {"id": 2, "name": "Lost Item 2", "date": "2024-02-09", "description": "Lost item description 2"}
]

dummy_found_items = [
    {"id": 1, "name": "Found Item 1", "date": "2024-02-08", "description": "Found item description 1"},
    {"id": 2, "name": "Found Item 2", "date": "2024-02-07", "description": "Found item description 2"}
]

@app.route('/')
def index():
    return render_template('index.html', lost_items=dummy_lost_items, found_items=dummy_found_items)

@app.route('/report_lost', methods=['GET', 'POST'])
def report_lost():
    if request.method == 'POST':
        # Process form submission
        # Placeholder code for storing data in the database
        return redirect(url_for('index'))
    return render_template('report_lost.html')

@app.route('/report_found', methods=['GET', 'POST'])
def report_found():
    if request.method == 'POST':
        # Process form submission
        # Placeholder code for storing data in the database
        return redirect(url_for('index'))
    return render_template('report_found.html')

@app.route('/latest_items')
def latest_items_list():
    return render_template('latest_items.html', lost_items=dummy_lost_items, found_items=dummy_found_items)

@app.route('/item/<int:item_id>')
def item_details(item_id):
    # Placeholder code to retrieve item details from the database
    # For now, let's assume we have a function to fetch item details
    item = {"id": item_id, "name": "Sample Item", "date": "2024-02-10", "description": "Sample description", "status": "Lost"}
    return render_template('item_details.html', item=item)

if __name__ == '__main__':
    app.run(debug=True)
