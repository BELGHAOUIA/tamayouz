from sqlmodel import Field
from app.model.base_model import BaseModel


class School(BaseModel):
    school_name: str = Field()
    school_state: str = Field()
    school_principal: str = Field()

