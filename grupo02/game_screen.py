import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, BLUE, RED
from assets import carrega_arquivos

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0
    PLAYING = 1
    state = PLAYING

    tela = 'azul'
    tempo_da_ultima_mudanca = pygame.time.get_ticks()


    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        
        # Lógica para alternar as cores
        agora = pygame.time.get_ticks()
        if agora - tempo_da_ultima_mudanca > 2000:
            tempo_da_ultima_mudanca = agora
            if tela == 'azul':
                tela = 'vermelha'
            else:
                tela = 'azul'

        if tela == 'azul':
            window.fill(BLUE)
            memorize=dicionario_de_arquivos['font_media'].render('Memorize...', True, (0,0,0))
            window.blit(memorize,(450-(memorize.get_rect().width)/2,150))
        else:
            window.fill(RED)
        window.blit(dicionario_de_arquivos['input'],(450-(dicionario_de_arquivos['input'].get_rect().width)/2,350-(dicionario_de_arquivos['input'].get_rect().height)/2))
        pygame.display.update()  # Mostra o novo frame para o jogador

    return state
