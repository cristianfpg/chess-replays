import sys
import os

# Add the parent directory to sys.path to allow imports from 'app'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlmodel import Session
from app.infrastructure.database import engine, create_db_and_tables
from app.application.match_service import MatchService

def seed():
    print("Initializing database...")
    create_db_and_tables()

    pgn_path = os.path.join(os.path.dirname(__file__), "twic1622.pgn")
    if not os.path.exists(pgn_path):
        print(f"Error: PGN file not found at {pgn_path}")
        return

    print(f"Reading PGN file: {pgn_path}")
    with open(pgn_path, "r", encoding="utf-8") as f:
        content = f.read()

    print("Importing matches...")
    with Session(engine) as session:
        service = MatchService(session)
        count = service.process_pgn_content(content)
        print(f"Successfully imported {count} matches.")

if __name__ == "__main__":
    seed()
