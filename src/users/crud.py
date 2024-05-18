from sqlalchemy.orm import Session
from users import models, schemas

import uuid
from typing import Optional

def create_user(db: Session, user: schemas.CreateUser) -> Optional[models.usersT]:
    accessToken = str(uuid.uuid4())[:8]
    db.user = models.usersT(login=user.login, password=user.password, accessToken=accessToken)
    db.add(db.user)
    db.commit()
    db.refresh(db.user)
    return db.user

def find_user(db: Session, login: str) -> Optional[models.usersT]:
    user = db.query(models.usersT).filter_by(login=login).first()
    return user
