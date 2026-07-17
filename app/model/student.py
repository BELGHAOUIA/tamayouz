from sqlmodel import Field
from app.model.base_model import BaseModel


class Student(BaseModel, table=True):
    full_name: str = Field()
    birth_date: date = Field()
    birth_place: str = Field()
    unique_idenifier: str = Field()