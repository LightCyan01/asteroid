import pygame
from constants import *

print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")
      

def main():
    pygame.init()
    
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()
    dt = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, "black")
        
        # updates the full display Surface to the screen
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        
        

if __name__ == "__main__":
    main()
