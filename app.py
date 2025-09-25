from flask import Flask, render_template, request

app = Flask(__name__)

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char in "!@#$%^&*()-_=+[]{};:,.<>?/|`~" for char in password):
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength == 3:
        return "Moderate"
    else:
        return "Strong"

@app.route("/", methods=["GET", "POST"])
def index():
    strength = None
    if request.method == "POST":
        password = request.form.get("password")
        strength = check_password_strength(password)
    return render_template("index.html", strength=strength)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char in "!@#$%^&*()-_=+[]{};:,.<>?/|`~" for char in password):
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength == 3:
        return "Moderate"
    else:
        return "Strong"

@app.route("/", methods=["GET", "POST"])
def index():
    strength = None
    if request.method == "POST":
        password = request.form.get("password")
        strength = check_password_strength(password)
    return render_template("index.html", strength=strength)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char in "!@#$%^&*()-_=+[]{};:,.<>?/|`~" for char in password):
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength == 3:
        return "Moderate"
    elif strength >= 4:
        return "Strong"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    password = ""
    if request.method == "POST":
        password = request.form.get("password")
        result = check_password_strength(password)
    return render_template("index.html", result=result, password=password)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char in "!@#$%^&*()-_=+[]{};:,.<>?/|`~" for char in password):
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength == 3:
        return "Moderate"
    else:
        return "Strong"

@app.route("/", methods=["GET", "POST"])
def index():
    strength = ""
    if request.method == "POST":
        password = request.form["password"]
        strength = check_password_strength(password)
    return render_template("index.html", strength=strength)

if __name__ == "__main__":
    app.run(debug=True)

