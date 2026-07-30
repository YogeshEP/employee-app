from flask import Flask, render_template

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Samarit", "department": "IT"},
    {"id": 2, "name": "JP", "department": "HR"},
    {"id": 3, "name": "Yogesh", "department": "DevOps"},
    {"id": 4, "name": "Shreya", "department": "Computer"},
    {"id": 5, "name": "Piyu", "department": "Computer"},
    {"id": 6, "name": "Veda", "department": "Computer"}
]

@app.route("/")
def home():
    return render_template("index.html", employees=employees)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
