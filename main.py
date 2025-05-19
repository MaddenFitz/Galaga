import pygame
pygame.init()
from ship import Ship
from bullet import Bullet
import constants as c
from background import BG
from star import Star
from enemy_spawner import EnemySpawner
from enemy import Enemy
from enemy2 import Enemy2
from particle_spawner import ParticleSpawner
from score import Score
from Alert_box import Alertbox
from planet import Planet
# from Loading Screen import Logo


#display measurements
display = pygame.display.set_mode(c.DISPLAY_SIZE)
fps = 60
clock = pygame.time.Clock()
black = (0, 0, 0)

#object setups
#sprite group for backround
bg = BG()
bg_group = pygame.sprite.Group()
bg_group.add(bg)

planets = Planet()
planets_group = pygame.sprite.Group()
planets_group.add(bg)

#sprote group for Loading Screen
# logo = Logo()
# logo_group = pygame.sprite.Group()
# logo_group.add(logo)

#sprite group for star
star = Star()
star_group = pygame.sprite.Group()
star_group.add(star)

#sprite group for player
player = Ship()
sprite_group = pygame.sprite.Group()
sprite_group.add(player)

#enemy spawner 
enemy_spawner = EnemySpawner()
particle_spawner = ParticleSpawner()
Alert_box_group = pygame.sprite.Group()


#Running fps
running = True
while running:
    #Tick clock
    clock.tick(fps)
    
    #Handle events
    #the 'event' is for collecting data which the user input
    for event in pygame.event.get():
        #for if the user closes the program
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            quit()
        #movement inputs - key is being pressed 'down'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.vel_x = -player.speed
            elif event.key == pygame.K_RIGHT:
                player.vel_x = player.speed
            if event.key == pygame.K_SPACE:
                player.shoot()
        #stops actions when keys are released 'up'
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.vel_x = 0
            elif event.key == pygame.K_RIGHT:
                player.vel_x = 0
    
    #Update all the obejcts 
    bg_group.update()
    sprite_group.update()
    planets_group.update()
    enemy_spawner.update()
    particle_spawner.update()
    Alert_box_group.update()
    
    #Check collision 
    #the the 1st & 2nd argument are specifying the things
    #the 3rd and 4th argument are what we want to do with them T = remove, F = stay
    collided = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemy_group, True, False)
    for bullet, enemy in collided.items():
        enemy[0].get_hit()
        player.hud.score.update_score(enemy[0].score_value)
        if not enemy[0].is_invincible:
            particle_spawner.spawn_particles((bullet.rect.x, bullet.rect.y))
    collided = pygame.sprite.groupcollide(sprite_group, enemy_spawner.enemy_group, False, False)
    for player, enemy in collided.items():
        if not enemy[0].is_invincible and not player.is_invincible:
            player.get_hit()
            enemy[0].hp = 0
            enemy[0].get_hit()
    for enemy in enemy_spawner.enemy_group:
        collided = pygame.sprite.groupcollide(sprite_group, enemy.bullets, False, True)
        for player, bullet in collided.items():
            if not player.is_invincible:
                player.get_hit()
            
    #Check for game over
    if not player.is_alive:
        enemy_spawner.clear_enemies()
        Alert_box = Alertbox("GAME OVER")
        Alert_box_group.add(Alert_box)
    
    #Render the display
    display.fill(black)
    bg_group.draw(display)
    planets_group.draw(display)
    sprite_group.draw(display)
    player.bullets.draw(display)
    enemy_spawner.enemy_group.draw(display)
    for enemy in enemy_spawner.enemy_group:
        enemy.bullets.draw(display)
    # logo_group.draw(display)
    particle_spawner.particle_group.draw(display)
    player.hud_group.draw(display)
    player.hud.health_bar_group.draw(display)
    player.hud.score_group.draw(display)
    player.hud.icons_group.draw(display)
    Alert_box_group.draw(display)
    pygame.display.update()