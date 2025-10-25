from fastapi import FastAPI, Query

from fastapi.middleware.cors import CORSMiddleware

from typing import List, Optional

import csv

 

app = FastAPI()

 

# Enable CORS

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],   # allow all origins

    allow_methods=["GET"], # allow only GET

    allow_headers=["*"],

)

 

# Load CSV data

students_data = []

csv_file_path = r"C:\Users\rguna\Downloads\q-fastapi.csv"

 

with open(csv_file_path, newline="", encoding="utf-8") as csvfile:

    reader = csv.DictReader(csvfile)

    for row in reader:

        students_data.append({

            "studentId": int(row["studentId"]),

            "class": row["class"]

        })

 

@app.get("/api")

def get_students(class_: Optional[List[str]] = Query(None, alias="class")):

    """

    Returns all students if no ?class= param is given.

    If ?class=1A&class=1B is given, return only those classes.

    Keeps same row order as CSV file.

    """

    if class_:

        filtered = [s for s in students_data if s["class"] in class_]

        return {"students": filtered}

    return {"students": students_data}