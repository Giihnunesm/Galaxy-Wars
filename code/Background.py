from code.Entity import Entity
from code.Const import WIN_WIDTH, ENTITY_SPEED

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED.get(name, 1) # Obtém a velocidade ou usa 1 como padrão

    def move(self, scroll_x):
        self.rect.x += scroll_x
        # Lógica para repetição contínua
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
        elif self.rect.left >= WIN_WIDTH:
            self.rect.right = 0