from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from ..base import Base


class CharacterActor(Base):
    __tablename__ = "characters_actors"

    character_id = Column(
        UUID(as_uuid=True),
        ForeignKey("characters.id", ondelete='CASCADE', onupdate="CASCADE"),
        primary_key=True,
        nullable=False
    )
    person_id = Column(
        UUID(as_uuid=True),
        ForeignKey("persons.id", ondelete='CASCADE', onupdate="CASCADE"),
        primary_key=True,
        nullable=False
    )
    