import chess.pgn
import io
from typing import List
from sqlmodel import Session
from app.domain.match import Match

class MatchService:
    def __init__(self, session: Session):
        self.session = session

    def process_pgn_content(self, pgn_content: str):
        """
        Parses PGN content and saves matches to the database.
        """
        pgn = io.StringIO(pgn_content)
        matches_processed = 0
        
        while True:
            # Parse the next game from the PGN file
            game = chess.pgn.read_game(pgn)
            if game is None:
                break  # End of file

            # Extract headers
            headers = game.headers
            
            # Helper to safely get int
            def get_int(key, default=0):
                val = headers.get(key, str(default))
                try:
                    return int(val)
                except ValueError:
                    return default

            # Helper to safely get float
            def get_float(key, default=0.0):
                val = headers.get(key, str(default))
                try:
                    return float(val)
                except ValueError:
                    return default

            # Create Match object
            # Note: Mapping PGN headers to our Match model fields
            match = Match(
                event=headers.get("Event", "Unknown"),
                site=headers.get("Site", "Unknown"),
                date=headers.get("Date", "Unknown"),
                round=get_float("Round"),
                white=headers.get("White", "Unknown"),
                black=headers.get("Black", "Unknown"),
                result=headers.get("Result", "*"),
                whiteTitle=headers.get("WhiteTitle", ""),
                blackTitle=headers.get("BlackTitle", ""),
                whiteElo=get_int("WhiteElo"),
                blackElo=get_int("BlackElo"),
                eco=headers.get("ECO", ""),
                opening=headers.get("Opening", ""),
                whiteFideId=get_int("WhiteFideId"),
                blackFideId=get_int("BlackFideId"),
                eventDate=headers.get("EventDate", ""),
                pgn=str(game) # Saving the reconstructed PGN or raw? str(game) gives PGN string
            )

            self.session.add(match)
            matches_processed += 1
        
        self.session.commit()
        return matches_processed
