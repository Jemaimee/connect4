from enum import Enum

from enums import Cell, GameState



class Game:
    def __init__(self):
        self.grid = Grid()
        self.player = None
        self.gamestate = GameState.STOPPED
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
                        self.gamestate = GameState.WIN


class Grid:
    def __init__(self):
        self.board = None

    def add_piece(self, color, y, x):
        self.board[y][x] = color

    def drop_piece(self, color, x):
        for line in self.board[::-1]:
            if line[x] == Cell.EMPTY:
                line[x] = color
                break

    def create_board(self):
        self.board =  [[Cell.EMPTY for j in range(7)] for i in range(6)]


