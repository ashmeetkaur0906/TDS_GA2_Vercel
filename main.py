from fastapi import FastAPI
import json
import os

# Initialize FastAPI app
app = FastAPI()

# Load the marks data
with open('marks.json') as f:
    marks_data = json.load(f)

@app.get("/api")
def get_marks(name: list[str]):
    marks = []
    for n in name:
        # Get the marks for each student
        student_marks = marks_data.get(n)
        if student_marks is not None:
            marks.append(student_marks)
        else:
            marks.append("Not found")  # If student is not in the data
    return {"marks": marks}
