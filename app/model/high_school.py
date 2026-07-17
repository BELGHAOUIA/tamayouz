from app.model.school import School
from sqlmodel import Field

class HighSchool(School, table=True):
   type: str = Field()