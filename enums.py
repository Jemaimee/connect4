from enum import Enum

class Cell(Enum):
    EMPTY = 0
    RED = 1
    YELLOW = 2

class GameState(Enum):
    RUNNING = 0
    STOPPED = 1
    WIN = 2