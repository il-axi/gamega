import pygame

class Ino(pygame.sprite.Sprite):
    """класс 1 пришельца"""
    def __init__(self, screen):
        """иниц. и задаем нач. позицию"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ino.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width  # ширина
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """вывод ино на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """перемещение пришельцев"""
        self.y += 0.1
        self.rect.y = self.y


