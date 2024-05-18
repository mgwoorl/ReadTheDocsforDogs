from sqlalchemy import Integer, String, Column
from database import BaseDBModel

class usersT(BaseDBModel):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, unique=True, index=True)
    password = Column(String, unique=False, index=False)
    accessToken = Column(String, unique=False, index=False)
