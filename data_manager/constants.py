from enum import Enum

DB_NAME = "tfm_games.db"
DB_URL = f"sqlite:///{DB_NAME}"
GAMES_TABLE_NAME = "games"

class COLORS(Enum):
    RED = 1,
    GREEN = 2,
    YELLOW = 3,
    BLUE = 4,
    GREY = 5,
    PURPLE = 6,
    ORANGE = 7,
    PINK = 8


