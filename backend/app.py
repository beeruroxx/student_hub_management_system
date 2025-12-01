from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client.studenthub


# -----------------------
# GET ALL STUDENTS
# -----------------------
@app.route("/students", methods=["GET"])
def get_students():
    students = list(db.students.find({}, {"_id": 0}))
    return jsonify(students)


# -----------------------
# ADD NEW STUDENT
# -----------------------
@app.route("/students", methods=["POST"])
def add_student():
    data = request.json

    # auto-generate ID
    last = db.students.find_one(sort=[("id", -1)])
    next_id = 1 if not last else last["id"] + 1

    new_student = {
        "id": next_id,
        "name": data["name"],
        "course": data["course"],
        "year": data["year"],
        "subjects": data.get("subjects", [])
    }

    db.students.insert_one(new_student)
    return jsonify({"message": "Student added", "id": next_id})


# -----------------------
# UPDATE STUDENT
# -----------------------
@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.json

    db.students.update_one({"id": student_id}, {"$set": data})

    return jsonify({"message": "Student updated"})


# -----------------------
# DELETE STUDENT
# -----------------------
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    db.students.delete_one({"id": student_id})
    return jsonify({"message": "Student deleted"})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
