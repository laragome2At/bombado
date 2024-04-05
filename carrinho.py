import pygame
import random
import sys

pygame.init()

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Desviar dos Obstáculos")

personagem_imagem = pygame.image.load('imagens/personagem.png')
obstaculo_imagem = pygame.image.load('imagens/obstaculo.png')

nova_largura = 100
nova_altura = 100
personagem_imagem = pygame.transform.scale(personagem_imagem, (nova_largura, nova_altura))

nova_largura = 100
nova_altura = 100
obstaculo_imagem = pygame.transform.scale(personagem_imagem, (nova_largura, nova_altura))

personagem_posicao_x = largura_tela // 2 - personagem_imagem.get_width() // 2
personagem_posicao_y = altura_tela - personagem_imagem.get_height() 

obstaculo_posicao_x = random.randint(0, largura_tela - obstaculo_imagem.get_width())
obstaculo_posicao_y = -obstaculo_imagem.get_height()
obstaculo_velocidade = 2

jogo_ativo = True

while True:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and personagem_posicao_x > 0:
        personagem_posicao_x -= 5
    if teclas[pygame.K_RIGHT] and personagem_posicao_x < largura_tela - personagem_imagem.get_width():
        personagem_posicao_x += 5

    obstaculo_posicao_y += obstaculo_velocidade

    personagem_rect = pygame.Rect(personagem_posicao_x, personagem_posicao_y, personagem_imagem.get_width(), personagem_imagem.get_height())
    obstaculo_rect = pygame.Rect(obstaculo_posicao_x, obstaculo_posicao_y, obstaculo_imagem.get_width(), obstaculo_imagem.get_height())
    if personagem_rect.colliderect(obstaculo_rect):
        jogo_ativo = False

    if obstaculo_posicao_y > altura_tela:
        obstaculo_posicao_x = random.randint(0, largura_tela - obstaculo_imagem.get_width())
        obstaculo_posicao_y = -obstaculo_imagem.get_height()
    
    tela.fill(BRANCO)
    tela.blit(personagem_imagem, (personagem_posicao_x, personagem_posicao_y))
    tela.blit(obstaculo_imagem, (obstaculo_posicao_x, obstaculo_posicao_y))
    pygame.display.flip()

    if not jogo_ativo:
        tela.fill(BRANCO)
        fonte = pygame.font.Font (None, 36)
        mensagem = fonte.render("Game Over! Pressione R para jogar novamente ou Q para sair.", True, PRETO)
        tela.blit(mensagem, (largura_tela // 2 - mensagem.get_width() // 2, altura_tela // 2 - mensagem.get_height() // 2))
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    jogo_ativo = True
                    personagem_posicao_x = largura_tela // 2 - personagem_imagem.get_width() // 2
                    personagem_posicao_y = altura_tela - personagem_imagem.get_height()
                    obstaculo_posicao_x = random.randint(0, largura_tela - obstaculo_imagem.get_width())
                    obstaculo_posicao_y = -obstaculo_imagem.get_height()
                elif evento.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()