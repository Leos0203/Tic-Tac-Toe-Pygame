import pygame
from pygame.locals import *
from pygame.mixer import *
from game import Game
from settings import *
from support import exit


def main():
    # Set up
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()

    # Window
    screen = pygame.display.set_mode(window_resolution)
    title = 'Mashup'
    pygame.display.set_caption(title)

    # Game
    game = Game(screen)

    # Loop
    while True:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                game.tic_tac_toe.added = False
                game.settings.added = False

        # Fill the screen
        screen.fill('black')

        # Game
        game.run()

        # Update the screen
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
