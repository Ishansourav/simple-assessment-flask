import csv
import json
from io import TextIOWrapper

def parse_csv(file):
    """
    Parses an uploaded CSV file into a list of [Index #, Value] pairs.
    Raises ValueError on failure.
    """
    try:
        csv_file = TextIOWrapper(file, encoding='utf-8')
        reader = csv.reader(csv_file)
        return [[row[0], int(row[1])] for row in reader if len(row) >= 2]
    except Exception as e:
        raise ValueError("Invalid CSV format") from e

def parse_json(file):
    """
    Parses an uploaded JSON file into a list of [Index #, Value] pairs.
    Raises ValueError on failure.
    """
    try:
        json_data = json.load(file)
        return [[item["Index #"], int(item["Value"])] for item in json_data]
    except Exception as e:
        raise ValueError("Invalid JSON format") from e

def load_json(filepath):
    """
    Loads a JSON file from a local filepath and parses it into [Index #, Value] pairs.
    Returns an empty list on failure.
    """
    try:
        with open(filepath, 'r') as f:
            raw_data = json.load(f)
            return [[item["Index #"], int(item["Value"])] for item in raw_data]
    except Exception:
        return []
