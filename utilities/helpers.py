import random
import json

def generate_email():
    return f"user{random.randint(1000,9999)}@test.com"


def load_test_data(file_path):
    with open(file_path) as f:
        return json.load(f)