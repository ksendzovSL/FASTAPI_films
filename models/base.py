from pydantic import BaseModel as Base


class BaseModel(Base):
    class Config:
        orm_mode = True
