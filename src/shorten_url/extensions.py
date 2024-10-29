from flask_sqlalchemy import SQLAlchemy
from . import models

database = SQLAlchemy(model_class=models.ModelBase)
