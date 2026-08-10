from sqlmodel import Field
from app.model.base_model import BaseModel


class ClassLevel(BaseModel, table=True):
   class_level: str = Field()
   