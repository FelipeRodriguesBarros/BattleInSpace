import sys
import pygame
from Configurações import Settings

def run_game():
    pygame.init()
    configuracoesDoJogo = Settings()


    screen = pygame.display.set_mode((configuracoesDoJogo.screen_height))
    pygame.display.set_caption("Invasao Alienigena")
    # Escreva o seu código aqui :-)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()

run_game()

