#!/usr/bin/python3


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items = data.get('items', [])
    except Exception as e:
        print("Error reading items.json: {}".format(e))
        items = []
    return render_template('items.html', items=items)

def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def read_csv(file_path):
    products = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error_message = None

    if source == 'json':
        try:
            products = read_json('products.json')
        except Exception as e:
            error_message = "Error reading JSON file: {}".format(e)
    elif source == 'csv':
        try:
            products = read_csv('products.csv')
        except Exception as e:
            error_message = "Error reading CSV file: {}".format(e)
    else:
        error_message = "Wrong source"

    if not error_message and product_id is not None:
        products = [product for product in products if product['id'] ==
                    product_id]
        if not products:
            error_message = "Product not found"

    return render_template(
        'product_display.html', products=products, error_message=error_message)

@app.route('/products')
def display_products():
    source = request.args.get('source', 'json')  # Par défaut, source est 'json'

    if source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Products')
            products = cursor.fetchall()
            conn.close()

            # Convertir la liste de tuples en liste de dictionnaires
            products = [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in products]

            return render_template('product_display.html', products=products, error_message=None)

        except sqlite3.Error as e:
            error_message = f"Database error: {e}"
            return render_template('product_display.html', products=None, error_message=error_message)

    else:
        error_message = "Wrong source: Please use 'json', 'csv', or 'sql' as source parameter."
        return render_template('product_display.html', products=None, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
