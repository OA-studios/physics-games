import pygame, math, sys

from random import randint

background_colour = (0,0,0)
(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
running = True

ang=0

ballx=400
bally=100

lunx=400
lunny=65


def x(angle,magnitude):
	return math.cos(angle)*magnitude

def y(angle,magnitude):
	return math.sin(angle)*magnitude

def draw():
	pygame.draw.circle(screen,(255,255,0), (width//2, height//2), 28)




class Planet(object):
	def __init__(self,x=0,y=0,size=10,colour=(255,255,255),speed=0.001,orbRadius=100,atmos=(False,0),trail=False,vx=0,vy=0): # atmos: atmos[0]=true/false, atmos[1] = colour
		self.x=x
		self.y=y
		self.angle=0
		self.size=size
		self.colour=colour
		self.speed=speed
		self.orbitRadius=orbRadius
		self.atmosphere=atmos
		self.trail=[(self.x,self.y)]
		self.trailTrue=trail
		self.count=0
		self.vx=vx
		self.vy=vy

	def draw(self):
		

		self.count+=1
		if self.trailTrue==True:

			for i in range(0,  min(len(self.trail),99)):
				pygame.draw.circle(screen,(2.55*(100-i),2.55*(100-i),2.55*(100-i)),(int(self.trail[i][0]),int(self.trail[i][1])),1)


		if self.atmosphere[0]==True:
			pygame.draw.circle(screen, self.atmosphere[1],(int(self.x),int(self.y)), int(self.size+self.size/5))
		pygame.draw.circle(screen, self.colour, (int(self.x),int(self.y)), self.size)


	def move(self,origin):
		self.angle+=1*self.speed
		self.x+=x(self.angle,self.orbitRadius)*self.speed+origin[0]+self.vx
		self.y+=y(self.angle,self.orbitRadius)*self.speed+origin[1]+self.vy

		
		if self.trailTrue==True and self.count%int(40)==0:
			self.trail.append((0,0))
			for i in reversed(range(0,  min(len(self.trail)-1,99))):
				self.trail[i+1]=self.trail[i]


			self.trail[0]=(self.x,self.y)  #x,y


	def xoff(self):
		return x(self.angle,self.orbitRadius)*self.speed

	def yoff(self):
		return y(self.angle,self.orbitRadius)*self.speed





# class GravityPlanet():
# 	def __init__(self,x,y,vx,vy,a,mass,size):
# 		self.x=x
# 		self.y=y
# 		self.vx=vx
# 		self.vy=vy
# 		self.a=a
# 		self.mass=mass
# 		self.size=size
# 		self.distance=1
# 		self.flip=True


# 	def draw(self):
# 		pygame.draw.circle(screen,(255,255,255),(int(self.x),int(self.y)),int(self.size))

# 	def move(self,m2,planet2x,planet2y): #m2 = the mass of the object you're orbiting around
# 		#self.a=((m2**2)*self.mass)/self.dist((self.x,self.y),(planet2x,planet2y))
# 		self.a=0.0007

# 		if self.y>400 and self.flip==True:
# 			self.a=-1*self.a
# 			self.flip=False



# 		self.vx+=self.a*((self.abs(self.x-planet2x))/(self.abs(self.x-planet2x)+self.abs(self.y-planet2y)))
# 		self.vy+=self.a*((self.abs(self.y-planet2y))/(self.abs(self.x-planet2x)+self.abs(self.y-planet2y)))
# 		self.x+=self.vx
# 		self.y+=self.vy

# 	def dist(self,a,b):#a and b take an x and a y parameter
		
# 		self.distance=math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
# 		if self.distance>0 or self.distance<0:
# 			return self.distance
# 		return 0.001


# 	def abs(self,n):
# 		if n>=0:
# 			return n
# 		return n*-1


# pa=GravityPlanet(400,100,0.1,0,0,0.1,10)
# psun=GravityPlanet(400,300,0,0,0,10,20)





	


planet=Planet(400,100,15,(0,255,0), 0.0001, 200,(True,(63, 165, 191, 0.37)),False)
moon=Planet(400,20,8,(222,222,222), 0.00075,80,(False,0),False)
moon2=Planet(400,60,4,(255,100,0),0.002,40,(False,0),True)
moon3=Planet(400,35,6,(0,0,255),0.0012,65,(False,0))
#moon4=Planet(300,200,25,(255,0,255),0.001,100,vx=0.05,vy=0)





running = True

while running:

	screen.fill(background_colour)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	draw()
	# pa.draw()
	# psun.draw()

	# pa.move((psun.mass),(psun.x),(psun.y))
	#psun.move((pa.mass),(pa.x),(pa.y))
	planet.draw()
	planet.move((0,0)) # add [thing your orbiting around].xoff/yoff()
	

	moon.draw()
	moon.move((planet.xoff(),planet.yoff()))

	moon2.draw()
	moon2.move((planet.xoff(),planet.yoff()))

	moon3.draw()
	moon3.move((planet.xoff(),planet.yoff()))

	#moon4.draw()
	#moon4.move((0,0))
	pygame.display.flip()