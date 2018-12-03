import pygame, random, math, time

class Ball(pygame.sprite.Sprite):
    dx = 0
    dy = 0
    x = 0
    y = 0
    direction = 0
    speed = 0

    def __init__(self, sp, srx, sry, radium, color):
        pygame.sprite.Sprite.__init__(self)
        self.speed = sp
        self.x = srx
        self.y = sry
        self.image = pygame.Surface([radium*2,radium*2])
        self.image.fill((255,255,255))
        pygame.draw.circle(self.image, color, (radium,radium), radium, 0)
        self.rect = self.image.get_rect()
        self.rect.center = (srx, sry)
        self.direction = random.randint(40,70)

    def update(self):
        radian = math.radians(self.direction)
        self.dx = self.speed*math.cos(radian)
        self.dy = -self.speed*math.sin(radian)
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.y = self.y
        if(self.rect.left <= 0 or self.rect.right >= screen.get_width()-10):
            self.bouncelr()
        elif(self.rect.top <= 10):
            self.rect.top = 10
            self.bounceup()
        if(self.rect.bottom >= screen.get_height()-10):
            return True
        else:
            return False
        
    def bounceup(self):
        self.direction = 360 - self.direction

    def bouncelr(self):
        self.direction = (180 - self.direction) % 360

class Brick(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([38,13])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y

class Pad(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('helloworld_python\\HTML\\wang.bmp')
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.x = int((screen.get_width() - self.rect.width)/2)
        self.rect.y = screen.get_height() - self.rect.height - 20
        print('add pad')

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > screen.get_width() - self.rect.width:
            self.rect.x = screen.get_width() - self.rect.width

def gameover(message):
    global running
    text = font1.render(message, 1, (255,0,255))
    screen.blit(text, (screen.get_width()/2 - 100,screen.get_height()/2 - 20))
    pygame.display.update()
    time.sleep(3)
    running = False

pygame.init()
score = 0
font = pygame.font.SysFont("SimHei", 20)
font1 = pygame.font.SysFont("SimHei", 32)
soundhit = pygame.mixer.Sound("helloworld_python\\HTML\\hit.wav")
soundpad = pygame.mixer.Sound("helloworld_python\\HTML\\pad.wav")
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("弹弹猪")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
allsprite = pygame.sprite.Group()
bricks = pygame.sprite.Group()
ball = Ball(10, 300, 350, 10, (255,0,0))
allsprite.add(ball)
pad = Pad()
allsprite.add(pad)
clock = pygame.time.Clock()
for row in range(0, 4):
    for column in range(0, 15):
        if row == 0 or row == 1:
            brick = Brick((0, 255, 0), column * 40 + 1, row * 15 + 1)
        if row == 2 or row == 3:
            brick = Brick((0, 0, 255), column * 40 + 1, row * 15 + 1)
        bricks.add(brick)
        allsprite.add(brick)

msgstr = "单机左键开始游戏"
playing = False
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    buttons = pygame.mouse.get_pressed()
    if buttons[0]:
        playing = True
    if playing == True:
        screen.blit(background, (0, 0))
        fail = ball.update()
        if fail:
            gameover('失败，再接再厉')
        pad.update()
        hitbrick = pygame.sprite.spritecollide(ball, bricks, True)
        if len(hitbrick) > 0:
            score += len(hitbrick)
            soundhit.play()
            ball.rect.y += 20
            ball.bounceup()
            if len(bricks) == 0:
                gameover('挑战成功')
        
        hitpad = pygame.sprite.collide_rect(ball, pad)
        if hitpad:
            soundpad.play()
            ball.bounceup()
        allsprite.draw(screen)
        msgstr = "得分：" + str(score)
    msg = font.render(msgstr, 1, (255,0,255))
    screen.blit(msg, (screen.get_width()/2 - 60, screen.get_height() - 20))
    pygame.display.update()
pygame.quit()