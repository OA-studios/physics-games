import sys,pygame,math
pygame.init()
 
size=width,height=800,600
screen=pygame.display.set_mode(size)
red=(255,0,0)
black=(0,0,0)
ball=0
maxsize=10
 
balls=[]
 
for x in range(10):
    balls.append(None)
 
def abs(n):
    if n < 0:
        return (-n)
    return n
 
def boncing(n,n2):
    if n<0:
        return n - abs(n2)
 
 
 
def sqr(n):
    return n*n
 
def getvf(b1, b2): #momentum calculations
    return [(((b1.mass - b2.mass) / (b1.mass + b2.mass)) * b1.vx + (((2 * b2.mass) / (b1.mass + b2.mass)) * b2.vx)),
    (((2 * b1.mass) / (b1.mass + b2.mass)) * b1.vx + ((b2.mass - b1.mass) / (b1.mass + b2.mass)) * b2.vx),  
    (((b1.mass - b2.mass) / (b1.mass + b2.mass)) * b1.vy + (((2 * b2.mass) / (b1.mass + b2.mass)) * b2.vy)),
    (((2 * b1.mass) / (b1.mass + b2.mass)) * b1.vy + ((b2.mass - b1.mass) / (b1.mass + b2.mass)) * b2.vy)
    ]
 
 
 
 
 
 
 
class Ball:
    def __init__(self, x, y,vx ,vy ):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.ydrag=0
        self.xdrag=0
        self.size=10
        self.mass=10
        self.lock=False
 
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (int(self.x),int(self.y)), int(self.size))
 
    def gravity(self):
        self.vy+=9.81/60/120/2
        #1m=120px
        self.y+=self.vy
        self.x+=self.vx
 
    def bounce(self):
 
        if self.y+self.size>540:#floor
            self.vy=-self.vy
 
            self.vy-=self.vy/1000#squishing when bouncing
            self.vx-=self.vx/3000
 
        if self.y+self.size>541:#floor reset
            self.y=540-self.size
            self.vy=0
 
        if self.x+self.size>800:#bounce right
            self.vx=-self.vx
 
        if self.x-self.size<0:#bounce left
            self.vx=-self.vx
 
    def drag(self):
        self.ydrag=self.vy/1500
        self.xdrag=self.vx/1500
 
        self.vy-=self.ydrag
        self.vx-=self.xdrag
 
    def collide(self,ball):
   
        if sqr(self.x - ball.x) + sqr(self.y - ball.y) < sqr(self.size + ball.size) and self.lock==False:
            self.lock=True
            return True
 
        self.lock=False
        return False
 
 
 
 
mouseX2=0
mouseY2=0
line=False
 
while True:
 
    mouseDown = False
    mouseUp=False
    (mouseX,mouseY)=pygame.mouse.get_pos()
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#makes game quit
            pygame.quit()
            sys.exit()
 
        if event.type == pygame.MOUSEBUTTONUP:
            (mouseX1, mouseY1) = pygame.mouse.get_pos()
            mouseUp=True
            line=False
 
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX2,mouseY2) = pygame.mouse.get_pos()
            mouseDown = True
            line= True
 
 
    if mouseUp == True:#creates the ball at mouse x and y
        for i in range(maxsize-1):
            balls[maxsize-i-1]=balls[maxsize-i-2]
        balls[0]=Ball(mouseX2, mouseY2, (mouseX2-mouseX1)/500, (mouseY2-mouseY1)/500)
 
 
 
 
 
       # balls.append(Ball(mouseX2, mouseY2, (mouseX2-mouseX1)/500, (mouseY2-mouseY1)/500))
 
    screen.fill(black)
 
    if line== True:#draws aim line
        pygame.draw.line(screen,(255,255,255), (mouseX,mouseY), (mouseX2,mouseY2))
       
 
 
 
 
 
 
 
   
    pygame.draw.line(screen, (255,255,255), (20,540), (20,420))#1m line
 
    pygame.draw.line(screen,(255,255,255), (5,465), (5,455))#1
    pygame.draw.line(screen,(255,255,255), (9,465),(9,455))#m1
    pygame.draw.line(screen,(255,255,255), (17,465),(17,455))#m3
    pygame.draw.line(screen,(255,255,255),(9,455),(13,465))#mdiagonal1
    pygame.draw.line(screen,(255,255,255),(13,465),(17,455))
 
    pygame.draw.line(screen, (255,255,255), (0,540), (800,540))#floor line
 
 
 
    for ball in balls:
        if ball is not None:
            ball.gravity()
            ball.drag()
            ball.bounce()
            ball.draw(screen)
            for ball1 in balls:
                if ball1 is not None:
                    same=False
                    if ball1.x == ball.x:
                        same=True
                   
                    if same==False:
                        if ball1.collide(ball)==True:
                            momentum=getvf(ball1,ball)
                            ball1.vx=momentum[0]
                            ball.vx=momentum[1]
                            ball1.vy=momentum[2]
                            ball.vy=momentum[3]
 
    pygame.display.flip()