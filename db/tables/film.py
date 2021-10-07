from sqlalchemy import Column, String, Integer, Date, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ..base import Base


class Film(Base):
    __tablename__ = "films"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    duration = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    release_date = Column(Date, nullable=False)
    rating = Column(Numeric(1), nullable=False)
    director_id = Column(
        UUID(as_uuid=True),
        ForeignKey("persons.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )

    director = relationship("Person")
