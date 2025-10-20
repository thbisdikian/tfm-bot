import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from . import constants
from .models.base import Base
from .models.games import Games

instance = None

def get_instance():
    global instance
    if instance is None:
        instance = SqlManager()
    return instance

class SqlManager:
    def __init__(self):
        self.db_url = constants.DB_URL
        self.engine = create_engine(self.db_url)
        self.Session = sessionmaker(bind=self.engine)
        self.create_tables()

    def add_game(self, game):
        """Add a new game to the database if it doesn't already exist."""
        logging.info(f"[SqlManager.add_game]: Adding game with ID {game.id} to the database.")
        with self.Session() as session:
            existing_game = session.get(Games, game.id)
            if existing_game is None:
                session.add(game)
                session.commit()
                logging.info(f"[SqlManager.add_game]: Game with ID {game.id} added successfully.")
            else:
                logging.info(f"[SqlManager.add_game]: Game with ID {game.id} already exists. Skipping insert.")

    def get_game(self, game_id):
        """Retrieve a game by its ID."""
        logging.info(f"[SqlManager.get_game]: Retrieving game with ID {game_id} from the database.")
        with self.Session() as session:
            return session.get(Games, game_id)

    def update_game(self, game):
        """Update an existing game in the database."""
        logging.info(f"[SqlManager.update_game]: Updating game with ID {game.id} in the database.")
        with self.Session() as session:
            session.merge(game)
            session.commit()
    
    def create_tables(self):
        """Create all tables in the database."""
        logging.info("[SqlManager.create_tables]: Creating all tables in the database.")
        Base.metadata.create_all(self.engine)

    def connect(self):
        """Establish a connection to the SQL database."""
        self.engine = create_engine(self.db_url, echo=True)
    
    def close(self):
        """Dispose of the database engine."""
        if self.engine:
            self.engine.dispose()
            self.engine = None