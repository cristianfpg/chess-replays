from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from sqlmodel import Session
from contextlib import asynccontextmanager

from app.domain.match import Match
from app.infrastructure.database import create_db_and_tables, get_session
from app.application.match_service import MatchService

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/matches/import")
async def import_pgn(file: UploadFile = File(...), session: Session = Depends(get_session)):
    """
    Upload a PGN file to import matches into the database.
    """
    if not file.filename.endswith('.pgn'):
        raise HTTPException(status_code=400, detail="File must be a .pgn file")
    
    content = await file.read()
    content_str = content.decode('utf-8')
    
    service = MatchService(session)
    count = service.process_pgn_content(content_str)
    
    return {"message": f"Successfully imported {count} matches."}

@app.get("/matches")
def get_matches(session: Session = Depends(get_session)):
    matches = session.query(Match).all()
    return matches
