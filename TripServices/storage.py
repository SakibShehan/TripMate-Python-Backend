import json
import os
import pathlib

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# DATA_FILE = os.path.join(BASE_DIR, "data", "trips_database.json")

BASE_DIR = pathlib.Path(__file__).parent.parent
DATA_FILE = BASE_DIR / "data" / "trips_database.json"


def load_trips():
    if not DATA_FILE.exists():
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:   # file is empty or broken
        return []


def save_trips(trips):
    with open(DATA_FILE, "w") as file:
        json.dump(trips, file, indent=4)