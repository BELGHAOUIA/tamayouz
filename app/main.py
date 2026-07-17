from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/student")
def get_students():
    try:
        response = supabase.table("student").select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/student")
def add_bulletin(bulletin):
    add_institute()
    add_student()
    add_classLevel()
    add_grades()

def add_student(student):
    try:
        response = supabase.table("student").create(student).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def add_institute():
    fo = 4