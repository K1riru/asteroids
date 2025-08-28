import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField



def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

# Containers
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids,updatable,drawable)
    Player.containers = (updatable,drawable)

# Create objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

# Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(black)

        updatable.update(dt)

        for drawn in drawable:
            drawn.draw(screen)


        pygame.display.flip()

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()