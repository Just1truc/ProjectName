import pygame


class Sol(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0,470,11,170)

    def afficher(self,surface):
        pygame.draw.rect(surface, (255,255,255), self.rect)
