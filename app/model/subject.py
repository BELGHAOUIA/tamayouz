from sqlmodel import Field


class Subject():
    name: str = Field()
    teacher_fullname: str = Field()