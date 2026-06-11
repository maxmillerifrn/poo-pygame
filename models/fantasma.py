from models.personagem import Personagem
from models.pacman import Pacman

class Fantasma(Personagem):
    def __init__(self,x,y,cor):
        super().__init__(x,y,cor)

    def perseguir(self, pacman:Pacman, blink=None):
        if self.x < pacman.x :
            self.mover('direita')
        elif self.x > pacman.x :
            self.mover('esquerda')
        elif self.y < pacman.y :
            self.mover('baixo')
        elif self.y > pacman.y :
            self.mover('cima')
