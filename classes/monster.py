import pygame
from game import Game

class Monster(pygame.sprite.Sprite):
    def __init__(self,game):
        global m
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.image = pygame.image.load("./assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,300)
        self.rect.y = 540
        self.velocity = random.randint(1,3)

    def damage(self, amount):
        global m
        self.health -= amount
        if self.health <= 0:
            #reapparaitre plus puissant
            self.rect.x = 1000 + random.randint(0,300)
            self.rect.y = 540
            self.health = 100
            self.velocity = random.randint(2,6)
            if m == 1:
                self.game.spawn_monster()
                m=0
            else: m += 0.25

    def update_health_bar(self, surface):

        #dessiner la barre de vie
        pygame.draw.rect(surface, (60,63,60), [self.rect.x +10,self.rect.y - 20,self.max_health,5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x +10,self.rect.y - 20,self.health,5])

    def forward(self):
        if not self.game.check_collision(self,self.game.all_player):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)
