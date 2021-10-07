from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from ..base import Base


class FilmGenre(Base):
    __tablename__ = "films_genres"

    film_id = Column(
        UUID(as_uuid=True),
        ForeignKey("films.id", ondelete='CASCADE', onupdate="CASCADE"),
        primary_key=True,
        nullable=False
    )
    film_genre_id = Column(
        String,
        ForeignKey("genres.id", ondelete='CASCADE', onupdate="CASCADE"),
        primary_key=True,
        nullable=False
    )
    