import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")
      

def main():
    pygame.init()
    
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, "black")
        
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision_detect(player):
                print("Game over!")
                sys.exit()
        
        for obj in drawable:
            obj.draw(screen)
        
        # updates the full display Surface to the screen
        pygame.display.flip()
        
        # limit frames to 60 fps
        dt = clock.tick(60) / 1000
    
    
        

if __name__ == "__main__":
    main()
