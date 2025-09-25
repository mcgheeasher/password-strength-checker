# Password Strength Checker 🔐

[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-orange)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

A simple **Flask web application** that checks the strength of a password.  
It tells you if your password is **Weak, Moderate, or Strong** based on rules like:
- Minimum length (8 characters)
- Includes numbers
- Includes uppercase and lowercase letters
- Includes special characters

---

## How to Run the Project

1. **Clone the repository**  
   ```bash
   git clone https://github.com/mcgheeasher/password-strength-checker.git
   cd password-strength-checker


2. **Create a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. **Install dependencies
   ```bash
   pip install -r requirements.txt
	
4. **Run the app
   ```bash
   python app.py

5. **Open your browser and go to:
   http://127.0.0.1:5000/

