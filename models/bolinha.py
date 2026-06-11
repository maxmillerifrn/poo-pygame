import pygame
from models.personagem import TAMANHO

class Bolinha:

    def __init__(self, x, y,grande=False):
        self.x = x
        self.y = y
        self.grande = grande
        self.comida = False
        self.valor = 50 if grande else 10

    def desenhar(self,tela, offset_x, offset_y):
        if self.comida:
            return
        cx = self.x * TAMANHO + TAMANHO //2 + offset_x
        cy = self.y * TAMANHO + TAMANHO //2 + offset_y
        raio = 6 if self.grande else 3
        #print(cx, cy, raio)
        pygame.draw.circle(tela,
                           color = (255,0,173),
                           center=(cx,cy),
                           radius=raio)

    def tem_colisao(self, personagem):
        if self.comida:
            return False
        elif self.x == personagem.x and self.y == personagem.y:
            return True
        return False