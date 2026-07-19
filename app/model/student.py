from app.model.base_model import BaseModel


class Student(BaseModel, table=True):
    fullname: str 
    birth_date: str 
    birth_place: str
    unique_idenifier: str