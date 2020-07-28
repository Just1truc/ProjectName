import pygame
from sol import Sol
from player import Player
from monster import Monster

class Game:


    def __init__(self):
        #defini si le jeu a commencé
        self.is_playing = False
        #generer notre joueur lorsqu'une nouvelle partie est créée
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        self.sol = Sol()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)