import pygame
import pygame.freetype
import random
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((800,700))
pygame.display.set_caption("звёздыныи выйны")
pygame.display.set_icon(pygame.image.load("ufo.png"))
cpaceimg=pygame.image.load("лораблькосм.png")
meterimg=pygame.image.load("vetr.png")
üüü=pygame.image.load("laser.png")
cpaceimg=pygame.transform.scale(cpaceimg,(70,70))
txt=pygame.freetype.Font(None,20)
gamestatus="game"
player_speed=0
class spaceship:
    def __init__(self,pos,img):
        self.HP=1000
        self.img=img
        self.rect=self.img.get_rect()
        self.rect.center=pos
    def damage(self,size):
        if size>0 and size<20:
            self.HP-=40
        if size>=20 and size < 50:
            self.HP-=60
        if size >=50 and size < 80:
            self.HP-=90
        if size >= 80 and size <120:
            self.HP-=140
        if self.HP<=0:
            print("sus")
    def fed(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:

            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        if keys[pygame.K_UP]:
            self.rect.y -= 5

        if keys[pygame.K_DOWN]:
            self.rect.y += 5

    def fgd(self):
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 700:
            self.rect.bottom = 700
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.left < 0:
            self.rect.left = 0

    def drow(self,pow):
        pow.blit(self.img,self.rect)
class cok(pygame.sprite.Sprite):
    def update(self):
        self.animation()
        self.rect.x+=self.speedx
        self.rect.y += self.speedy
        if self.rect.bottom > 700:
            self.kill()
    def animation(self):
        #self.image=pygame.transform.rotate(self.image,1)
        pass

    def __init__(self, pos, img):
        super().__init__()
        self.image=img
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speedx=random.randint(-1,1)
        self.speedy=4
class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()

groupmeter=pygame.sprite.Group()
gruplaser=pygame.sprite.Group()
spawn=pygame.USEREVENT
pygame.time.set_timer(spawn,1000)

chip=spaceship((400,600),cpaceimg)
running=True
while running:
    chip.fed()
    chip.fgd()
    for event in pygame.event.get():
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and len(gruplaser)<2:
                las=Laser(chip.rect.center,üüü)
                gruplaser.add(las)
            else:
                if gamestatus=="menu":
                    gamestatus="game"
                    chip.HP=1000


        if event.type == pygame.QUIT:
            running = False
        if event.type==spawn:
            a=random.randint(20, 100)
            meterimg1=pygame.transform.scale(meterimg,(a,a))
            meter=cok((random.randint(2,800),-20),meterimg1)
            groupmeter.add(meter)
    if pygame.sprite.spritecollide(chip,groupmeter,False):
        m=(pygame.sprite.spritecollide(chip,groupmeter,True)[0])
        k=m.rect.right-m.rect.left
        chip.damage(k)
        if chip.HP<0:
            gamestatus="menu"
    for laser in gruplaser:
        if pygame.sprite.spritecollide(laser,groupmeter,True):
            chip.HP=chip.HP+50
            with open("record.txt","r")as file:
                rec=file.read()
                rec=int(rec)
            if rec<chip.HP:
                with open("record.txt", "w") as file:
                    file.write(str(chip.HP))
            laser.kill()
    screen.fill((0,0,0))
    if gamestatus=="game":
        with open("record.txt", "r") as file:
            rec = file.read()
        txt.render_to(screen, (150,100), "best score: "+str(rec), (255, 255, 255), )
        chip.drow(screen)
        txt.render_to(screen, (150, 50),"score: "+str(chip.HP), (255, 255, 255),)
        groupmeter.draw(screen)
        groupmeter.update()
        gruplaser.draw(screen)
        gruplaser.update()
    else:
        txt.render_to(screen,(400,350),"Game Over",(255,255,255))
    pygame.display.flip()
    clock.tick(60)