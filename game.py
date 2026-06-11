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
        self.fantasmas=[]
        self.bolinhas=[]
        self.labirinto=None
        self.offset_x=0
        self.offset_y=0

    def _ligar_labirinto(self):
        if not self.labirinto:
            return
        for p in self._personagens():
            p.labirinto = self.labirinto

    def _personagens(self):
        todos = list(self.fantasmas)
        if self.pacman:
            todos.append(self.pacman)
        return todos

    def adicionar_pacman(self, pacman):
        self.pacman = pacman

    def adicionar_fantasma(self, fantasma):
        self.fantasmas.append(fantasma)

    def adicionar_bolinhas(self, bolinhas=None):
        if bolinhas is not None:
            self.bolinhas = bolinhas
        elif self.labirinto:
            self.bolinhas = self.labirinto.gerar_bolinhas()
        print(len(self.bolinhas))
        return self.bolinhas

    def adicionar_labirinto(self, labirinto=None):
        self.labirinto = labirinto if labirinto else Labirinto()
        self.offset_x = (self.largura - self.labirinto.largura())//2
        self.offset_y = (self.altura - self.labirinto.altura())//2
        self._ligar_labirinto()
        return self.labirinto

    #Aqui começa o fluxo do jogo

    def processa_evento(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                self.rodando = False

    def atualizar(self):
        self.contador += 1
        if self.contador % self.velocidade != 0:
            return
        if self.pacman:
            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_LEFT]:
                self.pacman.mover('esquerda')
            elif tecla[pygame.K_RIGHT]:
                self.pacman.mover('direita')
            elif tecla[pygame.K_UP]:
                self.pacman.mover('cima')
            elif tecla[pygame.K_DOWN]:
                self.pacman.mover('baixo')
        for f in self.fantasmas:
            if self.pacman:
                f.perseguir(self.pacman)
        if self.pacman:
            for b in self.bolinhas:
                if b.tem_colisao(self.pacman):
                    b.comida = True
                    self.pacman.pontos += b.valor

    def desenhar(self):
        self.tela.fill((0, 0, 0))
        if self.labirinto:
            self.labirinto.desenhar(self.tela,
                                    self.offset_x,
                                    self.offset_y)
        if self.pacman:
            self.pacman.atualizar_animacao()
            self.pacman.desenhar(self.tela,
                                 self.offset_x,
                                 self.offset_y)
        for f in self.fantasmas:
            f.atualizar_animacao()
            f.desenhar(self.tela,
                       self.offset_x,
                       self.offset_y)
        for b in self.bolinhas:
            b.desenhar(self.tela,
                       self.offset_x,
                       self.offset_y)
        pygame.display.update()

    def iniciar(self):
        while self.rodando:
            self.processa_evento()
            self.atualizar()
            self.desenhar()
            self.clock.tick(self.fps)
        pygame.quit()
