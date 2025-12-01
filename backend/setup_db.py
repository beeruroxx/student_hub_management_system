from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.studenthub

students = [
    {
        "id": 1,
        "name": "Arjun",
        "course": "BCA",
        "year": 1,
        "subjects": [
            {"name": "Maths", "marks": 85, "attendance": 90},
            {"name": "English", "marks": 78, "attendance": 88},
            {"name": "Computer Science", "marks": 92, "attendance": 95}
        ]
    },
    {
        "id": 2,
        "name": "Megha",
        "course": "BSc",
        "year": 2,
        "subjects": [
            {"name": "Physics", "marks": 81, "attendance": 86},
            {"name": "Chemistry", "marks": 75, "attendance": 82},
            {"name": "Maths", "marks": 89, "attendance": 91}
        ]
    },
    {
        "id": 3,
        "name": "Ravi",
        "course": "BCom",
        "year": 1,
        "subjects": [
            {"name": "Accounts", "marks": 90, "attendance": 97},
            {"name": "Business", "marks": 84, "attendance": 92},
            {"name": "Economics", "marks": 79, "attendance": 88}
        ]
    }
]

db.students.delete_many({})
db.students.insert_many(students)

print("Database seeded successfully with per-subject attendance!")
