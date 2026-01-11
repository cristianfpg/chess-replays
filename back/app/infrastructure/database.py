from sqlmodel import SQLModel, create_engine, Session

# Using a file-based SQLite database
# Note: relative path behavior might depend on where the app is run from.
# We'll use an absolute path or relative to CWD.
DATABASE_URL = "sqlite:///database.db"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
