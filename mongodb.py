from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["smarthire_ai"]

# Collections

users_collection = db["users"]

resume_collection = db["resumes"]

reports_collection = db["reports"]

print("MongoDB Connected Successfully")