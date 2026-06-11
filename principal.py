import pygame

from game import Jogo
from models.pacman import Pacman
from models.fantasma import Fantasma
from models.labirinto import Labirinto

if __name__ == '__main__':
    jogo = Jogo()
    jogo.adicionar_pacman(Pacman(13,16))
    jogo.adicionar_fantasma(Fantasma(11,10, 'Verde'))
    jogo.adicionar_labirinto(Labirinto())
    jogo.adicionar_bolinhas()
    jogo.iniciar()