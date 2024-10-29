from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class ModelBase(DeclarativeBase):
    """
    The base class for all SQLAlchemy declarative models
    """
    pass


database = SQLAlchemy(model_class=ModelBase)
