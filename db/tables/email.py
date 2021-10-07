from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ..base import Base


class Email(Base):
    __tablename__ = "emails"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    user_login = Column(
        String,
        ForeignKey("users.login", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )

    user = relationship("User")
    