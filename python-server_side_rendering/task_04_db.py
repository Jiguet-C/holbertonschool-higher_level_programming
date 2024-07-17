#!usr/bin/python3

from flask import Flask, rendertmp, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


def read_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    products = []
    for row in rows:
        products.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    prodid = request.args.get('id', type=int)

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql()
    else:
        return rendertmp('product_display.html', error="Wrong source")

    if prodid:
        products = [product for product in products if product['id'] == prodid]
        if not products:
            return rendertmp('product_display.html', error="Product not found")

    return rendertmp('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
