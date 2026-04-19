from enum import Enum

from enums import Cell, GameState



class Game:
    def __init__(self):
        self.grid = Grid()
        self.player = None
        self.gamestate = GameState.NOT_STARTED
        self.winner = None

    def start(self):
        self.grid.create_board()
        self.player = Cell.RED
        self.gamestate = GameState.RUNNING

    def stop(self):
        pass

    def switch_turn(self):
        if self.player == Cell.RED:
            self.player = Cell.YELLOW
        elif self.player == Cell.YELLOW:
            self.player = Cell.RED

    def check_game_state(self):

        directions = [
            (0,1),
            (1,0),
            (1,1),
            (1,-1)
        ]

        columns = len(self.grid.board[0])
        rows = len(self.grid.board)

        self.check_draw()

        for y in range(rows):
            for x in range(columns):

                player = self.grid.board[y][x]

                if player == Cell.EMPTY:
                    continue

                for sy, sx in directions:
                    winning = True

                    if not (0 <= y + sy * 3 < rows and 0 <= x + sx * 3 < columns):
                        continue

                    for i in range(4):

                        ny = y + sy * i
                        nx = x + sx * i
                        if self.grid.board[ny][nx] != player:
                            winning = False
                            break
                    if winning:
                        self.winner = player.name
                        self.gamestate = GameState.GAME_OVER
    def check_draw(self):
        if not Cell.EMPTY in self.grid.board[0]:
            self.gamestate = GameState.GAME_OVER

    def play(self, collum):
        if self.grid.ensure_not_full(collum):
            self.grid.drop_piece(self.player, collum)
            self.switch_turn()

class Grid:
    def __init__(self):
        self.board = None
        self.create_board()

    def add_piece(self, color, y, x):
        self.board[y][x] = color

    def drop_piece(self, color, x):
        for line in self.board[::-1]:
            if line[x] == Cell.EMPTY:
                line[x] = color
                break

    def ensure_not_full(self, x):
        for line in self.board:
            if line[x] == Cell.EMPTY:
                return True
        return False

    def create_board(self):
        self.board =  [[Cell.EMPTY for j in range(7)] for i in range(6)]


