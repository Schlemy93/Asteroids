import sys
import pygame
from constants import *
from player import *
from circleshape import *
from asteroidfield import *
def main():

	pygame.init()

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0
	asteroids = pygame.sprite.Group()
	asteroid_field = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	AsteroidField.containers = (updatable,)
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /  2)
	asteroidfield = AsteroidField()
	while True:
		screen.fill("black")
		
		for draw in drawable:
			draw.draw(screen)

		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
	
		dt = clock.tick(60) / 1000

		updatable.update(dt)

		for asteroid in asteroids:
			if asteroid.collisioncheck(player):
				print("Game Over!")
				sys.exit()
				pass













if __name__ == "__main__":
    main()
