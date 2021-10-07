from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from ..base import Base


class UserFavouriteFilm(Base):
    __tablename__ = "user_favourite_films"

    user_login = Column(
        String,
        ForeignKey("users.login", ondelete='CASCADE', onupdate="CASCADE"),
        primary_key=True,
        nullable=False
    )
    film_id = Column(
        UUID(as_uuid=True),
        ForeignKey("films.id", ondelete='CASCADE', onupdate="CASCADE"),
        primary_key=True,
        nullable=False
    )
    