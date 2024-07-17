#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route('/products')
def display_products():
    source = request.args.get('source', 'json')

    if source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Products')
            products = cursor.fetchall()
            conn.close()

            # Convertir la liste de tuples en liste de dictionnaires
            products = [{'id': row[0], 'name': row[1], 'category': row[2],
                         'price': row[3]} for row in products]

            return render_template('product_display.html', products=products,
                                   error_message=None)

        except sqlite3.Error as e:
            error_message = f"Database error: {e}"
            return render_template('product_display.html', products=None,
                                   error_message=error_message)

    else:
        error_message = ("Wrong source: Please use 'json', 'csv', or 'sql' as "
                         "source parameter.")
        return render_template('product_display.html', products=None,
                               error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True)
