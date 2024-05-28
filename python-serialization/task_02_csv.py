#!/usr/bin/python3
"""Convert csv to json"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to a JSON file."""
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
