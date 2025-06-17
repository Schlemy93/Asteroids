from circleshape import *
import main
from constants import *


class Shot(CircleShape):

	SHOT_RADIUS = 5
	def __init__(self, x, y, velocity):
		super().__init__(x, y, self.SHOT_RADIUS)
		self.velocity = velocity

	def draw(self, screen):
                pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width=2)
       

	def update(self, dt):
                self.position += self.velocity * dt

