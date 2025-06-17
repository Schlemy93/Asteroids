from circleshape import *
from constants import *
import random
class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width=2)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			random_angle = random.uniform(20, 50)
			new_velocity_1 = self.velocity.rotate(random_angle)
			new_velocity_2 = self.velocity.rotate(-random_angle)
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			asteroid_chunk_1 = Asteroid(self.position.x, self.position.y, new_radius)
			asteroid_chunk_1.velocity = new_velocity_1 *1.2
			asteroid_chunk_2 = Asteroid(self.position.x, self.position.y, new_radius)
			asteroid_chunk_2.velocity = new_velocity_2 * 1.2
