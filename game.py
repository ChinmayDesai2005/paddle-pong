import pygame
import os
from menu import *


class Game:
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.W_KEY, self.S_KEY, self.ESC_KEY = False, False, False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 700, 600
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = "8-BIT.TTF"
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)  # RGB Color values
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu
        self.main_running = False
        self.won = "Player0"

    def game_loop(self):
        while self.playing:
            self.check_events()
            while self.main_running == False:
                os.system('python Pong_Game_V2.py')
                self.main_running = True
            if self.START_KEY:
                self.playing = False
                self.main_running = False
            self.display.fill(self.BLACK)
            self.who_won()
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            print(self.won)
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_w:
                    self.W_KEY = True
                if event.key == pygame.K_s:
                    self.S_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.ESC_KEY =True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY , self.W_KEY, self.S_KEY, self.ESC_KEY = False, False, False, False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def who_won(self):
        if self.won == "Player1":
            self.draw_text("!!Player 1 Won!!", 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.draw_text("..Press Enter for Menu..", 12, self.DISPLAY_W/2, self.DISPLAY_H/2 + 20)
        elif self.won == "Player2":
            self.draw_text("!!Player 2 Won!!", 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.draw_text("..Press Enter for Menu..", 12, self.DISPLAY_W/2, self.DISPLAY_H/2 + 20)
        else:
            self.draw_text("!!Game Ended!!", 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.draw_text("..Press Enter for Menu..", 12, self.DISPLAY_W/2, self.DISPLAY_H/2 + 20)
