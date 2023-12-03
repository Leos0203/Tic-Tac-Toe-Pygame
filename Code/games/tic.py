import pygame
from settings import *


class Square(pygame.sprite.Sprite):
    def __init__(self, size, pos, color):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.filled = False
        self.mark = ''
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        pass


class Mark(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        pass


class TicTacToe():
    def __init__(self, screen, click, main_menu):
        self.screen = screen
        self.click_sound = click
        self.main_menu = main_menu

        self.font_size = 64
        self.frame_count = 0
        self.font = pygame.font.SysFont(
            '../Sprites/Fonts/Academy.ttf', self.font_size)
        self.set_up()

    def set_up(self):
        offset = [260, 260]
        self.points = [0, 0]
        self.point_added = False
        self.turns = 'X'
        self.added = False
        self.turn_count = 0
        self.x_spaces = []
        self.o_spaces = []
        self.square_group = pygame.sprite.Group()
        self.squares = list()
        self.mark_group = pygame.sprite.Group()
        for num in range(9):
            size = 250
            if num < 3:
                square = Square(
                    size, (15+(offset[0]*num), 15), (255, 255, 255))
                self.squares.append(square)
                self.square_group.add(square)
            if num < 6 and num > 2:
                square = Square(
                    size, (15+(offset[0]*(num-3)), offset[1]+15), (255, 255, 255))
                self.squares.append(square)
                self.square_group.add(square)
            if num <= 8 and num > 5:
                square = Square(
                    size, ((15+(offset[0]*(num-6)),
                           (offset[1]+7.5)*2)), (255, 255, 255))
                self.squares.append(square)
                self.square_group.add(square)

    def inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.main_menu.playing = False
            self.main_menu.on_menu = True
            self.main_menu.on_settings = False
            self.full_restart()

    def set_up_text(self):
        if self.turn_count % 2 == 0:
            self.turns = 'X'
        if self.turn_count % 2 == 1:
            self.turns = 'O'

        turns_text = self.font.render(
            str(self.turns).upper() + "'s turn", True, (255, 255, 255))
        self.screen.blit(
            turns_text, (window_resolution[0] // 2 - self.font_size, 850))

        x_points = self.font.render(
            'X: ' + str(self.points[0]), True, (255, 255, 255))
        o_points = self.font.render(
            'O: ' + str(self.points[1]), True, (255, 255, 255))
        self.screen.blit(x_points, (100, 900))
        self.screen.blit(o_points, (window_resolution[0]-200, 900))

    def reset_game(self):
        for square in self.squares:
            square.filled = False
            square.mark = ''
        self.mark_group.empty()
        self.x_spaces.clear()
        self.o_spaces.clear()
        self.point_added = False

    def full_restart(self):
        for square in self.squares:
            square.filled = False
            square.mark = ''
        self.mark_group.empty()
        self.x_spaces.clear()
        self.o_spaces.clear()
        self.point_added = False
        self.points = [0, 0]
        self.frame_count = 0

    def check_game_state(self):
        index = -1
        for square in self.squares:
            index += 1
            if square.filled == True:
                if square.mark == 'X':
                    if index not in self.x_spaces:
                        self.x_spaces.append(index)
                if square.mark == 'O':
                    if index not in self.o_spaces:
                        self.o_spaces.append(index)

        # SPACES
        if (0 in self.x_spaces):
            if (3 in self.x_spaces and 6 in self.x_spaces):
                if self.point_added == False:
                    self.points[0] += 1
                    self.point_added = True
                self.reset_game()
            if (1 in self.x_spaces and 2 in self.x_spaces):
                if self.point_added == False:
                    self.points[0] += 1
                    self.point_added = True
                self.reset_game()
            if (4 in self.x_spaces and 8 in self.x_spaces):
                if self.point_added == False:
                    self.points[0] += 1
                    self.point_added = True
                self.reset_game()
        if (0 in self.o_spaces):
            if (3 in self.o_spaces and 6 in self.o_spaces):
                if self.point_added == False:
                    self.points[1] += 1
                    self.point_added = True
                self.reset_game()
            if (1 in self.o_spaces and 2 in self.o_spaces):
                if self.point_added == False:
                    self.points[1] += 1
                    self.point_added = True
                self.reset_game()
            if (4 in self.o_spaces and 8 in self.o_spaces):
                if self.point_added == False:
                    self.points[1] += 1
                    self.point_added = True
                self.reset_game()
        if (1 in self.x_spaces and 4 in self.x_spaces and 7 in self.x_spaces):
            if self.point_added == False:
                self.points[0] += 1
                self.point_added = True
            self.reset_game()
        if (1 in self.o_spaces and 4 in self.o_spaces and 7 in self.o_spaces):
            if self.point_added == False:
                self.points[1] += 1
                self.point_added = True
            self.reset_game()
        if 2 in self.x_spaces:
            if (5 in self.x_spaces and 8 in self.x_spaces):
                if self.point_added == False:
                    self.points[0] += 1
                    self.point_added = True
                self.reset_game()
            if (4 in self.x_spaces and 6 in self.x_spaces):
                if self.point_added == False:
                    self.points[0] += 1
                    self.point_added = True
                self.reset_game()
        if 2 in self.o_spaces:
            if (5 in self.o_spaces and 8 in self.o_spaces):
                if self.point_added == False:
                    self.points[1] += 1
                    self.point_added = True
                self.reset_game()
            if (4 in self.o_spaces and 6 in self.o_spaces):
                if self.point_added == False:
                    self.points[1] += 1
                    self.point_added = True
                self.reset_game()
        if (3 in self.x_spaces and 4 in self.x_spaces and 5 in self.x_spaces):
            if self.point_added == False:
                self.points[0] += 1
                self.point_added = True
            self.reset_game()
        if (3 in self.o_spaces and 4 in self.o_spaces and 5 in self.o_spaces):
            if self.point_added == False:
                self.points[1] += 1
                self.point_added = True
            self.reset_game()
        if (6 in self.x_spaces and 7 in self.x_spaces and 8 in self.x_spaces):
            if self.point_added == False:
                self.points[0] += 1
                self.point_added = True
            self.reset_game()
        if (6 in self.o_spaces and 7 in self.o_spaces and 8 in self.o_spaces):
            if self.point_added == False:
                self.points[1] += 1
                self.point_added = True
            self.reset_game()
        if 0 in self.x_spaces or 0 in self.o_spaces:
            if 1 in self.x_spaces or 1 in self.o_spaces:
                if 2 in self.x_spaces or 2 in self.o_spaces:
                    if 3 in self.x_spaces or 3 in self.o_spaces:
                        if 4 in self.x_spaces or 4 in self.o_spaces:
                            if 5 in self.x_spaces or 5 in self.o_spaces:
                                if 6 in self.x_spaces or 6 in self.o_spaces:
                                    if 7 in self.x_spaces or 7 in self.o_spaces:
                                        if 8 in self.x_spaces or 8 in self.o_spaces:
                                            self.reset_game()

    def game_loop(self):
        self.inputs()
        if self.frame_count > 10:
            self.square_group.update()
            self.square_group.draw(self.screen)
            for square in self.squares:
                if square.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    if self.added == False and square.filled == False:
                        if self.turns == 'X' and square.filled == False:
                            mark = Mark(square.rect.center, '../Sprites/x.png')
                            self.mark_group.add(mark)
                            square.filled = True
                            square.mark = self.turns
                            self.click_sound.play()
                        if self.turns == 'O' and square.filled == False:
                            mark = Mark(square.rect.center, '../Sprites/o.png')
                            self.mark_group.add(mark)
                            square.filled = True
                            square.mark = self.turns
                            self.click_sound.play()
                        self.turn_count += 1
                        self.added = True
                        break
            self.mark_group.update()
            self.mark_group.draw(self.screen)
            self.set_up_text()
            self.check_game_state()
        self.frame_count += 1

    def run(self):
        self.game_loop()
