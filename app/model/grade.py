from app.model.enum.part import Part
from sqlmodel import Field


class Grade():
    part: Part = Part.FIRST
    grade: float = Field()
    rank: int = Field()