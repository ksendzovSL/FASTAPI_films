from sqlalchemy import Column, String, ForeignKey

from ..base import Base


class User(Base):
    __tablename__ = "users"

    login = Column(String, primary_key=True, nullable=False)
    password = Column(String, nullable=False)
    user_type_id = Column(
        String,
        ForeignKey("user_types.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )