from flask import Flask, render_template, request, jsonify
from utils.data_processor import compute_table2  # ✅ Now imported properly
import csv
import json
from io import TextIOWrapper

app = Flask(__name__)

# Optional fallback loader (from JSON file)
def load_json_data(filepath):
    try:
        with open(filepath, 'r') as f:
            raw_data = json.load(f)
            return [[item["Index #"], int(item["Value"])] for item in raw_data]
    except Exception:
        return []

@app.route("/", methods=["GET", "POST"])
def index():
    table_data = []
    computed = None

    if request.method == "POST":
        file = request.files.get("file")
        if file:
            filename = file.filename.lower()
            try:
                if filename.endswith(".csv"):
                    csv_file = TextIOWrapper(file, encoding='utf-8')
                    reader = csv.reader(csv_file)
                    table_data = [[row[0], int(row[1])] for row in reader if len(row) >= 2]

                elif filename.endswith(".json"):
                    json_data = json.load(file)
                    table_data = [[item["Index #"], int(item["Value"])] for item in json_data]

                computed = compute_table2(table_data)
                return jsonify({"table_data": table_data, "computed": computed})

            except Exception:
                return jsonify({"error": "File parsing error. Please check your format."})

        return jsonify({"error": "Unsupported file or no file uploaded."})

    else:
        table_data = load_json_data('table_data.json')  # Optional
        if table_data:
            computed = compute_table2(table_data)

    return render_template("index.html", table_data=table_data, computed=computed)

if __name__ == "__main__":
    app.run(debug=True)
