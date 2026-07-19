import json
from pathlib import Path
from google import genai
from PIL import Image
from app.repository.student_repository import StudentRepository

class BulletinService:
    def __init__(self, repo: StudentRepository, gemini_client: genai.Client):
        self.repo = repo
        self.client = gemini_client
        self.base_dir = Path(__file__).resolve().parent

    def process_and_save(self, image_path: str):
        img = Image.open(image_path)

        prompt_path = self.base_dir / "prompt.txt"
        with open(prompt_path, "r", encoding="utf-8") as f:
            prompt = f.read()

        response = self.client.models.generate_content(
            model="gemini-3.5-flash", contents=[img, prompt]
        )
        
        # Parse logic from your provided script
        data = json.loads(response.text.strip("`json\n"))
        print(data)
        student = {
            "fullname": data["studentName"],
            "birth_date": data["studentDateOfBirth"], 
            "birth_place": data["studentBirthPlace"],
            "unique_idenifier": data["studentUniqueIdentifier"]
        }
        # Save to DB
        return self.repo.save_student(student)