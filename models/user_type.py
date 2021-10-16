from pydantic import BaseModel


class UserType(BaseModel):
    id: str
    name: str
