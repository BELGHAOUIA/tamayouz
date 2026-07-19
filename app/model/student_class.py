from sqlmodel import Field
from app.model.base_model import BaseModel


class StudentClass(BaseModel, table=True):
    total_student_number: int = Field()
    class_number: str = Field()
    school_year: str = Field()
