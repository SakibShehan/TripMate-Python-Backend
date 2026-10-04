import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "trips_database.json")


def load_trips():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:   # file is empty or broken
        return []


def save_trips(trips):
    with open(DATA_FILE, "w") as file:
        json.dump(trips, file, indent=4)