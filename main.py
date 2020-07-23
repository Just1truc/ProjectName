import pygame
import random
pygame.init()
m=0

            
#generer la fenetre de notre jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080,720))
#creer l'arriere plan
background = pygame.image.load("./assets/bg.jpg")

#charger notre jeu
game = Game()

#charger le joueur
running = True

#boucle d'execution
while running:
    
    #appliquer l'arriere plan de notre jeu, les nombres sont le coordonées en x et y de ce que vois le joueur
    screen.blit(background, (0,-200))

    #appliquer l'image de mon joueur
    screen.blit(game.player.image,game.player.rect)
    
    #actualiser la barre de vie du joueur
    game.player.update_health_bar(screen)
    
    #recup les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()
        
    #recup les monstres
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)
    
    #appliquer l'ensemble des images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)
    
    game.all_monsters.draw(screen)
    
    
    #verifier si le joueur souhaite aller a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 930:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > -45:
        game.player.move_left()
          
    
    #mettre a jour la fenetre
    pygame.display.flip()
    #donner la possibiliter d'arreter le jeu par la croix
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # detecter que la touche espace est enclenchée
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        