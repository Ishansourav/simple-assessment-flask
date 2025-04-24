
# Simple Assessment Flask App

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Vercel Deployment](https://img.shields.io/badge/Live%20Demo-Vercel-success?logo=vercel)

A lightweight Flask-based web app that enables users to upload CSV or JSON files, process the data using Pandas, and generate a short report with computed Alpha, Beta, and Charlie values.

🔗 Live Demo: [https://simple-assessment-flask.onrender.com/](https://simple-assessment-flask.onrender.com/)

---

## 🚀 Features

- 📂 Upload CSV or JSON files
- 📊 Dynamic rendering of raw and computed tables
- 🧠 Computation of Alpha, Beta, Charlie using Pandas
- 📜 Short report generation
- 🧼 Clean UI using HTML, CSS, JS

---

## 💻 Language & Tool Roles

| Layer            | Tools                              |
|------------------|------------------------------------|
| Backend          | Flask 3.0.2, Pandas                |
| Frontend         | HTML5, CSS3, JavaScript            |
| Deployment       | Vercel, Heroku                     |
| Others           | Apache 2.0 License                 |

---

## 🔧 Folder Structure

```
simple-assessment/
├── app.py                # Flask backend logic
├── templates/
│   └── index.html        # Web UI
├── static/
│   ├── style.css         # Styles
│   └── script.js         # JS interactivity
├── utils/
│   ├── file_handler.py  # Handles CSV/JSON file uploads and parsing
│   └── data_processor.py # Contains functions for data calculation
├── assest/
│   ├── 1.png             # image -png format
|   ├── 2.png             # image
|   ├── 3.png             # image 
│   └── 4.png             
├── requirements.txt      # Python dependencies
├── Procfile              # For Heroku (optional)
├── .gitignore
├── setup.sh
└── README.md
```

---

## 🧠 System Architecture (Text View)

```
      +------------------------+
      |    User Interface      |
      |  (HTML, CSS, JS)       |
      +-----------+------------+
                  |
           File Upload
                  v
      +------------------------+
      |   Flask Backend (app.py) |
      | - Parsing & Processing  |
      | - Pandas Computation    |
      +-----------+------------+
                  |
             Response JSON
                  v
      +------------------------+
      |  Dynamic Table Render  |
      |   - Raw + Computed     |
      +------------------------+
```
---

## 🔧 System Layers

- Input Layer: File upload (CSV/JSON)
- Processing Layer: Data processing (Pandas)
- Output Layer: Dynamic Table Display & Calculation Results

---

## ⚙️ Setup Instructions (Local)

```bash
git clone https://github.com/Ishansourav/simple-assessment-flask.git
cd simple-assessment-flask

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
flask run
```

---

## 🌍 Deployment

Deployed on Vercel: [https://simple-assessment-flask.vercel.app](https://simple-assessment-flask.vercel.app)

Supports alternative deployment on Heroku, Render, Deta, PythonAnywhere.

---

<div class="section">
      <h2>🧠 Strategic Recommendations</h2>
      <ul>
            <li>Implement caching for faster data processing</li>
            <li>Enhance error handling and user feedback</li>
            <li>Consider adding a database for larger-scale data storage</li>
    </ul>
  </div>

---

## 🤝 Contributing

1. Fork the repo
2. Create your feature branch: git checkout -b feature/YourFeature
3. Commit your changes: git commit -m 'Add Some Feature'
4. Push to the branch: git push origin feature/YourFeature
5. Open a Pull Request

---

## 📜 License

This project is licensed under the Apache 2.0 License. See the LICENSE file for details.

---

## 🙏 Acknowledgements

- Flask & Pandas Community
- Vercel for hosting
- HTML/CSS/JS open-source resources

---
