from models.personagem import Personagem

class Pacman(Personagem):

    def __init__(self, x,y):
        super().__init__(x,y,cor='amarelo')
        self.vidas = 3
        self.pontos = 0

    def comer(self):
        self.pontos += 10

