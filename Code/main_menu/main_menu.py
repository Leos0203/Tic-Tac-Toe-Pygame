import pygame
from pygame.mixer import *
import settings
from support import exit


class Arrows(pygame.sprite.Sprite):
    def __init__(self, pos, color, size):
        super().__init__()
        self.color = color
        self.image = pygame.Surface((size, size))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        pass


class Settings():
    def __init__(self, screen, sound, main_menu):
        self.screen = screen
        self.click_sound = sound
        self.main_menu = main_menu

        self.font_size = 64
        self.added = False

        self.arrow_pos = (
            settings.window_resolution[0] / 2 + 100 + (self.font_size-64), settings.window_resolution[1] / 2 - 10)
        self.anti_aliasing_arrow = Arrows(self.arrow_pos, (102, 255, 102), 64)

    def inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.main_menu.playing = False
            self.main_menu.on_menu = True
            self.main_menu.on_settings = False

    def main_loop(self):
        self.inputs()
        self.font = pygame.font.SysFont(
            '../Sprites/Fonts/Academy.ttf', self.font_size)

        # Settings
        settings_size = 64
        settings_font = pygame.font.SysFont(
            '../Sprites/Fonts/Academy.ttf', settings_size)
        pos = (settings.window_resolution[0] / 2 -
               100, settings.window_resolution[1] - 850)
        settings_text = settings_font.render(
            'Settings', settings.anti_aliasing, (255, 255, 255))
        self.screen.blit(
            settings_text, pos)

        # Anti Aliasing
        pos = (settings.window_resolution[0] / 2 -
               200, settings.window_resolution[1] / 2)
        anti_aliasing_text = self.font.render(
            'Anti Aliasing', settings.anti_aliasing, (255, 255, 255))
        self.screen.blit(anti_aliasing_text, pos)

        if self.anti_aliasing_arrow.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                if settings.anti_aliasing == True and self.added == False:
                    settings.anti_aliasing = False
                    self.anti_aliasing_arrow.color = (255, 51, 51)
                    self.anti_aliasing_arrow.image.fill(
                        self.anti_aliasing_arrow.color)
                    self.click_sound.play()
                    self.added = True
                if settings.anti_aliasing == False and self.added == False:
                    settings.anti_aliasing = True
                    self.anti_aliasing_arrow.color = (102, 255, 102)
                    self.anti_aliasing_arrow.image.fill(
                        self.anti_aliasing_arrow.color)
                    self.click_sound.play()
                    self.added = True

        self.screen.blit(self.anti_aliasing_arrow.image, self.arrow_pos)

    def run(self):
        self.main_loop()


class MainMenu():
    def __init__(self, screen, click_sound):
        self.screen = screen
        self.click_sound = click_sound

        self.font_size = 64
        self.playing, self.on_menu, self.on_settings = False, True, False

        self.start_size, self.settings_size, self.exit_size = 64, 64, 64

    def normal_text(self):
        font = pygame.font.SysFont(
            '../Sprites/Fonts/Academy.ttf', self.font_size)
        main_menu_text = font.render(
            'Main Menu', settings.anti_aliasing, (255, 255, 255))
        self.screen.blit(
            main_menu_text, (settings.window_resolution[0] / 2 - 85, settings.window_resolution[1] - 850))

    def usable_text(self):
        # Start Button
        font = pygame.font.SysFont(
            '../Sprites/Fonts/Academy.ttf', self.start_size)
        pos = (settings.window_resolution[0] / 2 - 40 -
               (self.start_size-64), settings.window_resolution[1] / 2)
        start_text = font.render(
            'Start', settings.anti_aliasing, (255, 255, 255))
        start_rect = start_text.get_rect(topleft=pos)
        self.screen.blit(start_text, pos)
        if start_rect.collidepoint(pygame.mouse.get_pos()):
            if self.start_size < 104:
                self.start_size += 10

            if pygame.mouse.get_pressed()[0]:
                self.click_sound.play()
                self.playing = True
                self.on_menu = False
                self.on_settings = False
        else:
            if self.start_size > 64:
                self.start_size -= 10

        # Settings
        font = pygame.font.SysFont(
            '../Sprites/Fonts/Academy.ttf', self.settings_size)
        pos = (settings.window_resolution[0] / 2 - 75 - (
            self.settings_size-64), settings.window_resolution[1] / 2 + 100)
        settings_text = font.render(
            'Settings', settings.anti_aliasing, (255, 255, 255))
        settings_rect = settings_text.get_rect(topleft=pos)
        self.screen.blit(settings_text, pos)
        if settings_rect.collidepoint(pygame.mouse.get_pos()):
            if self.settings_size < 104:
                self.settings_size += 10

            if pygame.mouse.get_pressed()[0]:
                self.click_sound.play()
                self.playing = False
                self.on_menu = False
                self.on_settings = True
        else:
            if self.settings_size > 64:
                self.settings_size -= 10

        # Exit
        font = pygame.font.SysFont(
            '../Sprites/Fonts/Academy.ttf', self.exit_size)
        pos = (settings.window_resolution[0] / 2 - 40 - (
            self.exit_size-64), settings.window_resolution[1] / 2 + 200)
        exit_text = font.render(
            'Exit', settings.anti_aliasing, (255, 255, 255))
        exit_rect = settings_text.get_rect(topleft=pos)
        self.screen.blit(exit_text, pos)
        if exit_rect.collidepoint(pygame.mouse.get_pos()):
            if self.exit_size < 104:
                self.exit_size += 10

            if pygame.mouse.get_pressed()[0]:
                self.click_sound.play()
                exit()
        else:
            if self.exit_size > 64:
                self.exit_size -= 10

    def main_loop(self):
        self.normal_text()
        self.usable_text()

    def run(self):
        self.main_loop()
