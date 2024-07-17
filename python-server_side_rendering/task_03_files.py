#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
