from games.tic import TicTacToe
import pygame
from pygame.mixer import *
from main_menu.main_menu import MainMenu, Settings


class Game():
    def __init__(self, screen):
        self.screen = screen
        self.click_sound = pygame.mixer.Sound('../Sounds/click_effect.wav')

        self.main_menu = MainMenu(self.screen, self.click_sound)
        self.settings = Settings(self.screen, self.click_sound, self.main_menu)
        self.tic_tac_toe = TicTacToe(
            self.screen, self.click_sound, self.main_menu)

    def game_loop(self):
        # Tic Tac Toe
        self.tic_tac_toe.run()

    def main_menu_loop(self):
        self.main_menu.run()

    def settings_loop(self):
        self.settings.run()

    def run(self):
        if self.main_menu.playing:
            self.game_loop()
        if self.main_menu.on_menu:
            self.main_menu_loop()
        if self.main_menu.on_settings:
            self.settings_loop()
