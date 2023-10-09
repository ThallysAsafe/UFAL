import pygame
from pygame.locals import *

pygame.init()

# Configurações da janela
largura, altura = 800, 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Caixa de Perguntas e Respostas")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Fonte
fonte = pygame.font.Font(None, 32)

# Variáveis para perguntas e respostas
pergunta = ""
resposta = ""
input_ativo = False

executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            executando = False
        elif evento.type == KEYDOWN:
            if input_ativo:
                if evento.key == K_BACKSPACE:
                    pergunta = pergunta[:-1]
                elif evento.key == K_RETURN:
                    resposta = "Você perguntou: " + pergunta
                    pergunta = ""
                else:
                    pergunta += evento.unicode
        elif evento.type == MOUSEBUTTONDOWN:
            if pygame.Rect(250, 10, 300, 32).collidepoint(evento.pos):
                input_ativo = True
            else:
                input_ativo = False

    janela.fill(branco)

    # Renderiza a pergunta
    texto_pergunta = fonte.render("Digite sua pergunta:", True, preto)
    janela.blit(texto_pergunta, (10, 10))
    pygame.draw.rect(janela, preto, (250, 10, 300, 32), 2)
    texto_caixa_pergunta = fonte.render(pergunta, True, preto)
    janela.blit(texto_caixa_pergunta, (255, 10))

    # Renderiza a resposta
    if resposta:
        texto_resposta = fonte.render(resposta, True, preto)
        janela.blit(texto_resposta, (10, 50))

    pygame.display.flip()

pygame.quit()
