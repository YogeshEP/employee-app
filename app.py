from flask import Flask, render_template

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Rahul", "department": "IT"},
    {"id": 2, "name": "Priya", "department": "HR"},
    {"id": 3, "name": "Amit", "department": "Finance"}
]

@app.route("/")
def home():
    return render_template("index.html", employees=employees)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
