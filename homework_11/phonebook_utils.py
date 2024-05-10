import json
import os

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        return []

def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def create_json_file(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            json.dump([], file)
