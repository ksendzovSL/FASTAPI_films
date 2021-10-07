from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ..base import Base


class Character(Base):
    __tablename__ = "characters"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    comment = Column(String, nullable=True)
    film_id = Column(
        UUID(as_uuid=True),
        ForeignKey("films.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )
    
    film = relationship("Film")
    