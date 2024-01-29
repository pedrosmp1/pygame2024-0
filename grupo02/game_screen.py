import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, BLUE, RED
from assets import carrega_arquivos
import random


def sorteia_numeros(x):
    n=''
    for i in range(x):
        y=random.randint(0,9)
        n+=str(y)
    return n


def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0
    PLAYING = 1
    state = PLAYING

    tela = 'azul'
    tempo_da_ultima_mudanca = pygame.time.get_ticks()
    numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    x=1
    n=sorteia_numeros(x)
    vidas=3
    acertos=0
    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            if event.type==pygame.KEYDOWN and tela!='azul' and len(num_digitado)<x:
                if event.key == pygame.K_BACKSPACE:
                    num_digitado = num_digitado[:-1]
                elif event.unicode in numbers:
                    num_digitado+=event.unicode

            


        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        
        # Lógica para alternar as cores
        agora = pygame.time.get_ticks()
        if agora - tempo_da_ultima_mudanca > 3000:
            tempo_da_ultima_mudanca = agora
            if tela == 'azul':
                tela = 'vermelha'
                num_digitado=''
            else:
                if n==num_digitado:
                    acertos+=1
                    dicionario_de_arquivos['snd_vitoria'].play()
                else:
                    vidas-=1
                    dicionario_de_arquivos['snd_derrota'].play()
                    if vidas==0:
                        state=DONE
                tela = 'azul'
                x+=1
                n=sorteia_numeros(x)
        
        window.blit(dicionario_de_arquivos['input'],(450-(dicionario_de_arquivos['input'].get_rect().width)/2,350-(dicionario_de_arquivos['input'].get_rect().height)/2))
        if tela == 'azul':
            memorize=dicionario_de_arquivos['font_media'].render('Memorize...', True, (255,255,255))
            numero=dicionario_de_arquivos['font_media'].render(n, True, (255,255,255))
            window.blit(memorize,(450-(memorize.get_rect().width)/2,150))
            window.blit(numero,(450-(numero.get_rect().width)/2,250))
            


            
        else:
            digite=dicionario_de_arquivos['font_media'].render('Digite...', True, (255,255,255))
            window.blit(digite,(450-(digite.get_rect().width)/2,150))
            n_d=dicionario_de_arquivos['font_media'].render(num_digitado, True, (0,0,0))
            window.blit(n_d,(450-(n_d.get_rect().width)/2,350))
            
            
        vida=dicionario_de_arquivos['font'].render(f'vidas:{str(vidas)}', True, (255,255,255))
        window.blit(vida,(650,50))
        acerto=dicionario_de_arquivos['font'].render(f'acertos:{str(acertos)}', True, (255,255,255))
        window.blit(acerto,(650,80))
    # if state==DONE:
    #     fim = dicionario_de_arquivos['font_media'].render("Fim de Jogo!", True, (255, 255, 255))
    #     acerto=dicionario_de_arquivos['font'].render(f'acertos:{str(acertos)}', True, (255,255,255))

    #     window.blit(fim, (400,400))
    #     window.blit(acerto, (400,500))

            
        pygame.display.update()  # Mostra o novo frame para o jogador
    return state


    
    
        

    
