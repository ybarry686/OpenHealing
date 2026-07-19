from db.connection import engine, Base
from db import models

Base.metadata.create_all(engine)