import os
import pygame

TAMANHO = 24
ASSETS = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)
    ),"assets"
)

class Personagem:

    def __init__(self,x,y,cor):
        self.x = x
        self.y = y
        self.cor = cor
        self.direcao = 'direita'
        self.frame = 0
        self.labirinto = None
        self.sprites = {}
        self.carregar_sprites()

    def mover(self, direcao):
        self.direcao = direcao
        nx = self.x
        ny = self.y
        if direcao == 'cima':
            ny -=1
        elif direcao == 'baixo':
            ny +=1
        elif direcao == 'esquerda':
            nx -=1
        elif direcao == 'direita':
            nx +=1
        if (self.labirinto is None or
                self.labirinto.casa_livre(nx,ny)):
            self.x,self.y = nx,ny

    def carregar_sprites(self):
        nome = self.__class__.__name__.lower()
        direcoes = ["direita","esquerda","baixo","cima"]
        for direcao in direcoes:
            quadros = []
            for f in (0,1):
                caminho = os.path.join(ASSETS,
                f"{nome}_{direcao}_{f}.png")
                if os.path.exists(caminho):
                    img = pygame.image.load(caminho).convert_alpha()
                    img = pygame.transform.scale(img, (TAMANHO,TAMANHO))
                    quadros.append(img)
            self.sprites[direcao] = quadros

    def atualizar_animacao(self):
        self.frame += 1

    def sprite_atual(self):
        quadros = self.sprites.get(
            self.direcao,self.sprites['direita']
        )
        return quadros[(self.frame//5)%len(quadros)]

    def desenhar(self, tela, offset_x=0, offset_y=0):
        px = self.x*TAMANHO+offset_x
        py = self.y*TAMANHO+offset_y
        tela.blit(self.sprite_atual(), (px,py))
