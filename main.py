import pygame
import sys
from constants import *
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    score = 0

    # Initialize groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Sort objects
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    af = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        for obj in updatable:
            obj.update(dt)
        
        for ast in asteroids:
            if ast.is_colliding(player):
                print("Game over!")
                print(f"Score: {score}")
                sys.exit()
            for sh in shots:
                if ast.is_colliding(sh):
                    ast.split()
                    if ast.radius <= ASTEROID_MIN_RADIUS:
                        ast.kill()
                        score += 1
                    else:
                        ast.kill()


if __name__ == "__main__":
    main()
