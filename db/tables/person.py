from sqlalchemy import Column, String, Date
from sqlalchemy.dialects.postgresql import UUID

from ..base import Base


class Person(Base):
    __tablename__ = "person"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False
    )
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    