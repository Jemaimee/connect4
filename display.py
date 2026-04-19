import pygame

import settings
from enums import Cell, GameState

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

    def draw(self, board, gamestate, winner):

        self.board_surface.fill(settings.BOARD_COLOR)
        self.draw_cells(board)
        self.screen.blit(self.board_surface, (self.board_margin_left, self.board_margin_top))

        if gamestate == GameState.GAME_OVER:
            self.display_end_screen(winner)

        if gamestate == GameState.NOT_STARTED:
            self.display_menu()

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
        if winner:
            gamestate_content = f"{winner} HAS WON!"
        else:
            gamestate_content = "IT'S A DRAW!"
        gamestate_text = self.font.render(gamestate_content, 1, "white")
        gamestate_text_rect = gamestate_text.get_rect(center=(settings.WINDOW_WIDTH // 2, settings.WINDOW_HEIGHT//2))
        restart_text = self.font.render(f"click anywhere to restart", 1,"white")
        restart_text_rect = restart_text.get_rect(center=(settings.WINDOW_WIDTH // 2, 100))


        s = pygame.Surface((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        s.set_alpha(192)
        s.fill((0,0,0))

        self.screen.blit(s, (0,0))
        self.screen.blit(gamestate_text, gamestate_text_rect)
        self.screen.blit(restart_text, restart_text_rect)
    def display_menu(self):

        start_button_text = self.font.render("START",1, "white")
        start_button_rect = start_button_text.get_rect(center=(settings.WINDOW_WIDTH // 2, settings.WINDOW_HEIGHT//2))

        s = pygame.Surface((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        s.set_alpha(192)
        s.fill((0, 0, 0))

        self.screen.blit(s, (0, 0))
        self.screen.blit(start_button_text, start_button_rect)