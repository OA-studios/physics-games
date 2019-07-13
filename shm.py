import pygame , sys, math
from random import randint
 
background_colour = (0,0,0)
(width, height) = (1280,720)
screen = pygame.display.set_mode((width, height))


class Pendulum(object):
	def __init__(self,mass, length,origin=(width/2,height/2),screen=screen,size=10,g=9.81):
		self.origin=origin
		self.screen=screen
		self.length=length
		self.g=g
		self.x=self.origin[0]
		self.y=self.origin[1]+self.length
		self.w=math.sqrt(self.g/self.length)
		self.size=size
		self.s=0
		self.count=0
		self.t=0

	def draw(self,pivot):
		pygame.draw.circle(self.screen,(255,255,255),(int(self.x),int(self.y)),int(self.size))
		pygame.draw.line(self.screen,(255,255,255),(pivot),(int(self.x),int(self.y)))

	def physics(self,x=0):
		self.count+=1
		self.t=self.count/60
		self.s=math.sin(self.t*self.w+3.1415/2)
		self.x=self.s+self.x+x

def main():
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption('Simple harmonic motion')
	
	running = True

	pendulum=Pendulum(1,height/2,(width/2,height/5))
	pendulum2=Pendulum(1,height/4,(pendulum.x,pendulum.y))

	while running:
		screen.fill(background_colour)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				sys.exit(0)
		
		pendulum.draw((width/2,height/5))
		pendulum2.draw((pendulum.x,pendulum.y))
		pendulum.physics()
		pendulum2.physics(pendulum.s)

		pygame.display.flip()
		
if __name__ == "__main__":
	main()