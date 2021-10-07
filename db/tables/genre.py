from sqlalchemy import Column, String

from ..base import Base


class Genre(Base):
    __tablename__ = "genres"

    id = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)