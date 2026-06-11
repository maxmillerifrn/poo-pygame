import pygame
from models.pacman import Pacman
from models.fantasma import Fantasma
from models.bolinha import Bolinha
from models.labirinto import Labirinto

class Jogo:

    def __init__(self,
                 largura=800,
                 altura=600,
                 fps=60,
                 velocidade=6):
        self.largura = largura
        self.altura = altura
        self.fps = fps
        self.velocidade = velocidade
        pygame.init()
        self.tela = pygame.display.set_mode(
            (self.largura, self.altura)
        )
        pygame.display.set_caption("Pacman")
        self.clock = pygame.time.Clock()
        self.contador = 0
        self.rodando = True
        self.pacman=None
        self.fantasma=[]
        self.bolinhas=[]
        self.labirinto=None
        self.offset_x=0
        self.offset_y=0

    def _ligar_labirinto(self):
        if not self.labirinto:
            return

    def adicionar_pacman(self, pacman):
        self.pacman = pacman

    def adicionar_fantasma(self, fantasma):
        self.fantasmas.append(fantasma)