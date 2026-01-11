from sqlmodel import Field, SQLModel

class Match(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    event: str | None = None
    site: str | None = None
    date: str | None = None
    round: float | None = None
    white: str | None = None
    black: str | None = None
    result: str | None = None
    whiteTitle: str | None = None
    blackTitle: str | None = None
    whiteElo: int | None = None
    blackElo: int | None = None
    eco: str | None = None
    opening: str | None = None
    whiteFideId: int | None = None
    blackFideId: int | None = None
    eventDate: str | None = None
    pgn: str | None = None
