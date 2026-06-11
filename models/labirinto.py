import pygame
from models.personagem import TAMANHO
from models.bolinha import Bolinha
from models.mapas import MAPA_1
class Labirinto:
    def __init__(self,layout=None,cor = (33,33,33)):
        self.layout = layout if layout else MAPA_1
        self.cor = cor
        self.linhas = len(self.layout)
        self.colunas = max(
            len(linha) for linha in self.layout
        )

    def eh_parede(self, x, y):
        if y < 0 or y >= self.linhas:
            return False
        linha = self.layout[y]
        if x < 0 or x >= len(linha):
            return False
        return linha[x] == '#'

    def gerar_bolinhas(self):
        bolinhas = []
        for y,linha in enumerate(self.layout):
            for x,c in enumerate(linha):
                if c == '.':
                    bolinhas.append(Bolinha(x,y))
                elif c == 'o':
                    bolinhas.append(Bolinha(x,y,True))
        return bolinhas

    def largura(self):
        return self.colunas * TAMANHO
    def altura(self):
        return self.linhas * TAMANHO

    def desenhar(self,tela,offset_x,offset_y):
        for y, linha in enumerate(self.layout):
            for x, c in enumerate(linha):
                if c == '#':
                    cx = x * TAMANHO+offset_x
                    cy = y * TAMANHO+offset_y
                    rect = pygame.Rect(cx,cy,TAMANHO,TAMANHO)
                    pygame.draw.rect(tela,
                                     self.cor,
                                     rect,
                                     border_radius=4)