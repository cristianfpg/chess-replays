from typing import Union

from fastapi import FastAPI

from sqlmodel import Field, Session, SQLModel, create_engine

app = FastAPI()
engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/all_heroes")
def read_hero():
    with Session(engine) as session:
        heroes = session.query(Hero).all()
        return heroes

@app.get("/test")
def read_test():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.commit()
        return {"Test": "Success"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
