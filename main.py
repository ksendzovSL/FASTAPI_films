from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from db import pg_session, tables
from models import UserType

app = FastAPI()


@app.get("/user-types")
def read_user_types(
    db: Session = Depends(pg_session)
) -> UserType:
    result = db.query(tables.UserType).all()
    return result


@app.get("/user-types/{type_id}")
def read_user_type(
    type_id: str,
    db: Session = Depends(pg_session)
) -> UserType:
    result = (
        db.query(tables.UserType)
        .filter(tables.UserType.id == type_id)
        .first()
    )
    if result is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return result
