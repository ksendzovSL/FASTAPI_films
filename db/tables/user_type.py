from sqlalchemy import Column, String

from ..base import Base


class UserType(Base):
    __tablename__ = "user_types"

    id = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)