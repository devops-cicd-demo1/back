from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "George"},
    {"id": 2, "name": "Ahmed"},
    {"id": 3, "name": "Mohamed"}
]

@app.route("/")
def home():
    return "Backend is running"

@app.route("/api/students")
def get_students():
    return jsonify(students)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)