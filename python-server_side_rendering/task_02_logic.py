#!/usr/bin/python3

from flask import Flask, render_template
import json
import os


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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
