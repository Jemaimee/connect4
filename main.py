import pygame


import settings
from game import Game
from display import DisplayManager
from enums import GameState


pygame.init()
screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True
display = DisplayManager(screen)
game = Game()
game.start()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and game.gamestate == GameState.RUNNING:
            if event.button == 1:
                collum = display.screen_to_collum(event.pos[0])
                if collum != None:
                    game.grid.drop_piece(game.player, int(collum))
                    game.switch_turn()
        if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN) and game.gamestate == GameState.WIN:
            game.start()

    screen.fill(settings.BACKGROUND_COLOR)
    if game.gamestate == GameState.RUNNING:
        game.check_game_state()

    display.draw(game.grid.board)
    if game.gamestate == GameState.WIN:
        display.display_end_screen(game.winner)



    pygame.display.flip()

    clock.tick(60)

if __name__ == "__main__":
    pass