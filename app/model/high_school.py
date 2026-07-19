from app.model.enum.institute_type import InstituteType
from app.model.school import School
from sqlmodel import Field

class HighSchool(School, table=True):
   type: InstituteType = InstituteType.HIGH_SCHOOL