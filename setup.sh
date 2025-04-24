#!/bin/bash

echo "🚀 Setting up your Flask project..."

# Create virtual environment
python3 -m venv venv

# Activate environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

echo "✅ Project is up and running at http://127.0.0.1:5000"
