from app.model.base_model import BaseModel
from app.model.class_level import *


class Student(BaseModel, table=True):
    fullname: str 
    birth_date: str 
    birth_place: str
    unique_identifier: [{class_level: None, idenitifier: ""}]