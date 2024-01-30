import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, BLUE, RED
from assets import carrega_arquivos
import random


def tela_fim(window,pontos,rank):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0
    PLAYING = 1
    state = PLAYING

    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
        window.fill(RED)
        fim = dicionario_de_arquivos['font_media'].render("Fim de Jogo!", True, (255, 255, 255))
        acerto=dicionario_de_arquivos['font'].render(f'acertos:{str(pontos)}', True, (255,255,255))
        window.blit(fim, (100,80))
        window.blit(acerto, (600,80))
        ranking=dicionario_de_arquivos['font_media'].render("Ranking:", True, (255, 255, 255))
        window.blit(ranking,(300,150))
        for i in range(len(rank[:10])):
            ranking_pontos=dicionario_de_arquivos['font'].render(f"{rank[i]}", True, (255, 255, 255))
            window.blit(ranking_pontos,(300,200+i*50))


        
        # ----- Gera saídas
          # Preenche com a cor branca
        
            
            
                
        pygame.display.update()  # Mostra o novo frame para o jogador
    return state


    
    
        

    
