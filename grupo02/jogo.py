
import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from init_screen import init_screen
from game_screen import game_screen
from tela_fim import tela_fim



pygame.init()
pygame.mixer.init()


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Nome do seu jogo')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state,pontos,rank = game_screen(window)
    elif state=='fim':
        state=tela_fim(window,pontos,rank)
    else:
        state = QUIT


pygame.quit() 

