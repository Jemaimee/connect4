import pygame

import settings
from enums import Cell

class DisplayManager:
    CELL_COLOR ={
        Cell.YELLOW: "#FFE135",
        Cell.RED: "#E60026",
        Cell.EMPTY: "#005AD9"
    }
    def __init__(self, screen):
        self.screen = screen
        self.board_width = settings.CELL_SIZE * settings.BOARD_COLUMN + settings.CELL_MARGIN * (settings.BOARD_COLUMN + 1)
        self.board_height = settings.CELL_SIZE * settings.BOARD_ROW + settings.CELL_MARGIN * (settings.BOARD_ROW + 1)
        self.board_surface = pygame.Surface((
           self.board_width,
           self.board_height
        ))
        self.board_margin_left = (settings.WINDOW_WIDTH - self.board_width) / 2
        self.board_margin_top = (settings.WINDOW_HEIGHT - self.board_height) / 2
        self.collum_width = self.board_width // settings.BOARD_COLUMN
        self.font = pygame.font.SysFont("arial",50)

    def draw(self, board):

        self.board_surface.fill(settings.BOARD_COLOR)
        self.draw_cells(board)
        self.screen.blit(self.board_surface, (self.board_margin_left, self.board_margin_top))

    def draw_cells(self, board):
        for y in range(settings.BOARD_ROW):
            for x in range(settings.BOARD_COLUMN):
                cell_rect = pygame.Rect(
                    settings.CELL_MARGIN * (x+1) + settings.CELL_SIZE * x,
                    settings.CELL_MARGIN * (y+1) + settings.CELL_SIZE * y,
                    settings.CELL_SIZE,
                    settings.CELL_SIZE

                )
                pygame.draw.rect(self.board_surface, self.CELL_COLOR[board[y][x]], cell_rect, border_radius=settings.CELL_SIZE // 2)

    def screen_to_collum(self, screen_x):
        return max(0, min((screen_x - self.board_margin_left) // self.collum_width, settings.BOARD_ROW))

    def display_end_screen(self,winner):
        text = self.font.render(f"{winner} HAS WON!", 1,"white")
        text_rect = text.get_rect(center=(settings.WINDOW_WIDTH // 2, settings.WINDOW_HEIGHT//2))

        s = pygame.Surface((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        s.set_alpha(192)
        s.fill((0,0,0))

        self.screen.blit(s, (0,0))
        self.screen.blit(text, text_rect)