from sqlmodel import Field
from app.model.base_model import BaseModel


class School(BaseModel):
    name: str = Field()
    state: str = Field()
    principal: str = Field()

