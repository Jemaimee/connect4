from enum import Enum

class Cell(Enum):
    EMPTY = 0
    RED = 1
    YELLOW = 2

class GameState(Enum):
    RUNNING = 0
    NOT_STARTED = 1
    GAME_OVER = 2
