#!/usr/bin/env python3
import requests
import csv

def fetch_and_print_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    print(f'Status Code: {response.status_code}')

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Create a list of dictionaries with id, title, and body
        structured_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        # Define the CSV file column names
        fieldnames = ['id', 'title', 'body']

        # Write to CSV file
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_data)
