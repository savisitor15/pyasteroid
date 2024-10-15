# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    # Initialize groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gc = pygame.time.Clock()
    dt = 0
    # Assign groups
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    # Spawn the player and asteroid field
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    af = AsteroidField()
    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0)) 
        for thing in updateable:
            thing.update(dt)
        for asteroid in asteroids:
            if asteroid.collission(player):
                print("Game Over!")
                return
            for shot in shots:
                if asteroid.collission(shot):
                    shot.kill()
                    asteroid.kill()
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = gc.tick(60) / 1000


if __name__ == "__main__":
    main()