from typing import Union

from fastapi import FastAPI

from sqlmodel import Field, Session, SQLModel, create_engine

app = FastAPI()
engine = create_engine("sqlite:///database.db", echo=True)
SQLModel.metadata.create_all(engine)

class Match(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    event: str
    site: str
    date: str
    round: float
    white: str
    black: str
    result: str
    whiteTitle: str
    blackTitle: str
    whiteElo: int
    blackElo: int
    eco: str
    opening: str
    whiteFideId: int
    blackFideId: int
    eventDate: str
    pgn: str

@app.get("/matches")
def get_matches():
    with Session(engine) as session:
        matches = session.query(Match).all()
        return matches
