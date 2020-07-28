import pygame
from projectiles import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        #les pv
        self.game = game
        self.health = 100
        self.max_health = 100
        #les points d'attack
        self.attack = 10
        #vitesse de déplacement
        self.velocity = 1
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("../assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 500

    def launch_projectile(self):
        #creer une nouvelle instanceProjectile()
        self.all_projectiles.add(Projectile(self))



    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def update_health_bar(self, surface):

        #dessiner la barre de vie
        pygame.draw.rect(surface, (60,63,60), [self.rect.x +50,self.rect.y +20,self.max_health,5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x +50,self.rect.y + 20,self.health,5])
    def damage(self, amount):
        if self.health-amount>amount:
            self.health -= amount