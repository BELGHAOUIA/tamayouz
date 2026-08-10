from fastapi import FastAPI, HTTPException

from app.repository.student_repository import StudentRepository
from app.services.bulletin_service import BulletinService
from fastapi import FastAPI, UploadFile, Depends
from app.core.database import supabase_client
from app.core.ocr import gemini_client

app = FastAPI()


origins = [
    "http://localhost:5173",
    "*"                       # Use ["*"] temporarily for easy testing, or specify domains
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # Allows requests from these origins
    allow_credentials=True,
    allow_methods=["*"],         # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],         # Allows all headers
)

@app.get("/student")
def get_students():
    try:
        response = supabase_client.table("student").select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_service():
    repo = StudentRepository(supabase_client)
    return BulletinService(repo, gemini_client)

@app.post("/upload-student")
async def upload_student(file: UploadFile, service: BulletinService = Depends(get_service)):
    try:
        # Save temp file, process it, then delete
        file_path = f"temp_{file.filename}"
        with open(file_path, "wb") as f:
            f.write(await file.read())
            
        result = service.process_and_save(file_path)
        return {"status": "success", "data": result.data}
    except Exception as e:
        return {"status": "error", "message": str(e)}