from __future__ import annotations
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import ModelBase


class RedirectURL(ModelBase):
    """
    A long URL that users will ultimately be redirected to
    """
    __tablename__ = "redirects"

    redirect_id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(String(2048), unique=True)
    aliases: Mapped[list[Alias]] = relationship(back_populates="redirect_url")


class Alias(ModelBase):
    """
    A short alias for a long URL
    """
    __tablename__ = "aliases"

    alias_id: Mapped[int] = mapped_column(primary_key=True)
    key: Mapped[str] = mapped_column(String(32), unique=True)
    redirect_id: Mapped[int] = mapped_column(ForeignKey("redirects.redirect_id"))
    redirect_url: Mapped[RedirectURL] = relationship(back_populates="aliases")
