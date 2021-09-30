from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import random

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
)

from tkinter import * 
from tkinter import messagebox

from game_classes import Colored_coin, Empty_space, Blocked_space, Column_color
from game_parametres import coin_info, object_colors, samples, field_setup, coin_separation, endgame



class Game:
    def __init__(self, width = 600, height = 700):
        self.width = width
        self.height = height
        self.screen = setup_screen(width, height)
        self.colors = initiate_colors()
        self.coins = initiate_field(self.colors, self.screen)

    
    def start(self):
        create_message()
        run_game(self)


def initiate_colors():
    colors = [
        [object_colors.BLACK for _ in range(coin_info.COIN_COLUMN)] 
        for _ in range(coin_info.COIN_ROW)
    ]

    sample = random.sample(samples.COLOR_SAMPLE, 3)
    
    for k, (i,j) in enumerate(field_setup.SET_COLORS):
        colors[i][j] = sample[k]

    sample_repeats = random.sample(samples.COLOR_SAMPLE_REPEATS, 15)

    k = 0
    for i in range(1, coin_info.COIN_ROW):
        for j in range(coin_info.COIN_COLUMN):
            if j in field_setup.INITIAL_COIN_SETUP:
                colors[i][j] = sample_repeats[k]
                k += 1
            elif (i,j) in field_setup.INITIAL_EMPTYSPACE_SETUP:
                colors[i][j] = object_colors.GREY
    
    return colors

def check_endgame_condition(coins):
    check = endgame.MISMATCH
    column_colors = [Column_color(object_colors.BLACK, (0,0), 0) for _ in range(coin_info.COIN_COLUMN)]

    k = 0
    for coin in coins:
        if isinstance(coin, Column_color):
            column_colors[k] = coin
            k += 2
            continue
        if not isinstance(coin, Colored_coin):
            continue
        if isinstance(coin, Colored_coin) and coin.color == column_colors[coin.column].color:
            check = endgame.MATCH
        else: check = endgame.MISMATCH
        if check == endgame.MISMATCH:
            return False
    return True

def initiate_field(colors, screen):
    position = (coin_separation.SEPARATION, coin_separation.SEPARATION)
    coins = []
    k = 0
    for i in range(coin_info.COIN_ROW):
        for j in range(coin_info.COIN_COLUMN):
            if colors[i][j] in samples.COLOR_SAMPLE and i != 0:
                coins.append(Colored_coin(colors[i][j], position, j))
            elif colors[i][j] in samples.COLOR_SAMPLE and i == 0 and (i,j) in field_setup.SET_COLORS:
                coins.append(Column_color(colors[i][j], position, j))
            elif colors[i][j] == object_colors.GREY:
                coins.append(Empty_space(position, j))
            elif (i,j) not in field_setup.EMPTY:
                coins.append(Blocked_space(position))

            if (i,j) in field_setup.EMPTY:
                screen.blit(coins[k].s(), position)
                k += 1
            position = (position[0] + coin_info.COIN_DIMENSION + coin_separation.SEPARATION, position[1])
            
        position = (coin_separation.SEPARATION, position[1] + coin_info.COIN_DIMENSION + coin_separation.SEPARATION)
    return coins

def move_avalible(chosen_coin_1, chosen_coin_2, coins):
    if chosen_coin_1 != -1 and chosen_coin_2 != -1 and type(coins[chosen_coin_2]) is type(Empty_space((0,0), 0)) and type(coins[chosen_coin_1]) is type(Colored_coin(object_colors.RED, (0,0), 0)) \
        and ((abs(coins[chosen_coin_2].position[0] - coins[chosen_coin_1].position[0]) == coin_separation.CENTERS_SEPARATION and abs(coins[chosen_coin_2].position[1] - coins[chosen_coin_1].position[1]) == 0.0) or \
        (abs(coins[chosen_coin_2].position[1] - coins[chosen_coin_1].position[1]) == coin_separation.CENTERS_SEPARATION and abs(coins[chosen_coin_2].position[0] - coins[chosen_coin_1].position[0]) == 0.0)):
        return True
    return False
                    
def run_game(self):

    coin_chosen = False
    running = True

    chosen_coin_1, chosen_coin_2 = coin_info.COIN_NOT_CHOSEN,coin_info.COIN_NOT_CHOSEN
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not coin_chosen:
                pos = pygame.mouse.get_pos()
                for i in range(len(self.coins)):
                    if self.coins[i].rect.collidepoint(pos) and isinstance(self.coins[i], Colored_coin):
                        chosen_coin_1 = i
                        coin_chosen = True
            if event.type == pygame.MOUSEBUTTONUP and coin_chosen:
                pos = pygame.mouse.get_pos()
                for i in range(len(self.coins)):
                    if self.coins[i].rect.collidepoint(pos) and isinstance(self.coins[i], Empty_space):
                        chosen_coin_2 = i
                
                if move_avalible(chosen_coin_1, chosen_coin_2, self.coins):
                    self.coins[chosen_coin_2].rect, self.coins[chosen_coin_1].rect = self.coins[chosen_coin_1].rect, self.coins[chosen_coin_2].rect
                    self.coins[chosen_coin_2].position, self.coins[chosen_coin_1].position = self.coins[chosen_coin_1].position, self.coins[chosen_coin_2].position
                    self.coins[chosen_coin_2].column, self.coins[chosen_coin_1].column = self.coins[chosen_coin_1].column, self.coins[chosen_coin_2].column

                    chosen_coin_1, chosen_coin_2 = coin_info.COIN_NOT_CHOSEN,coin_info.COIN_NOT_CHOSEN

                coin_chosen = False
                
        
        self.screen.fill((255, 255, 255))
        for coin in self.coins:
            self.screen.blit(coin.s(), coin.position)

        pygame.display.flip()
        

        if check_endgame_condition(self.coins):
            self.screen.fill((255, 255, 255))
            messagebox.showinfo('Message', 'Congratulations! You won!')
            running = False
    
    pygame.quit()

def create_message():
    root = Tk()
    root.geometry("300x200")  
    root.withdraw()
    
    messagebox.showinfo('Instructions','Hello there!\n To start playing this game read instruction below:\n \
            1. To move color blocks click on one and drag it on near empty space (grey blocks).\n \
            2. Black blocks represent blocked space, you can\'t move colored blocks there.\n \
            3. In order to win you need to align color blocks in 3 columns according to color blocks in first row.\n \
            4. If you want to exit press ESC or close the window.\n \
                Good luck and have fun!')

def setup_screen(width, height):
    pygame.init()
    screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption('Test game Nightmare Realm')

    return screen

if __name__ == "__main__":
    game = Game()
    game.start()