import json

with open('people.json') as f:
    data = json.load(f)

def get_students(str):
    return data

def get_students_id(student_id: str):
    for students in data['students']:
        if student_id == students['id']:
            return('id:',students['id'],'firstname:',students['firstname'],'lastname:',students['lastname'],)













