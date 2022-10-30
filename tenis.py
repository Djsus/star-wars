import pygame
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((800,500))
pygame.display.set_caption("тенис 2 игрока")
pygame.display.set_icon(pygame.image.load("ping-pong-png-pic-5a3b88f4c0a853.5267748015138511247891.jpg"))
a=pygame.mixer.Sound("asdcx.wav")
pygame.mixer.init()


running=True
player=pygame.Rect(20,220,20,80)
bot=pygame.Rect(750,200,20,80)
ball=pygame.Rect(400,250,20,20)
scor=[0,0]
txt=pygame.freetype.Font(None,20)
player_speed2=0
player_speed=0
ball_speedX=1
ball_speedY=1
def dfs():
    if player.top<0:
        player.top=0
    if player.bottom>500:
        player.bottom=500
def dfs1():
    if bot.top<0:
        bot.top=0
    if bot.bottom>500:
        bot.bottom=500


def dfs2():
    global ball_speedX
    global ball_speedY
    if ball.right > 800:
        ball.center = (400, 250)
        ball_speedX = 1
        ball_speedY = 1
        scor[0] += 1
    if ball.left < 0:
        ball.center = (400, 250)
        ball_speedX = 1
        ball_speedY = 1
        scor[1] += 1

    if ball.top < 0:
        ball_speedY = - ball_speedY
    if ball.bottom > 500:
        ball_speedY = - ball_speedY
    if player.colliderect(ball):
        ball_speedX = - ball_speedX
    if bot.colliderect(ball):
        ball_speedX =- ball_speedX
        a.play()

    ball.x += ball_speedX
    ball.y += ball_speedY

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_speed -= 2
            elif event.key == pygame.K_s:
                player_speed += 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_speed += 2
            elif event.key == pygame.K_s:
                player_speed -= 2

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                player_speed2-=2
            elif event.key==pygame.K_DOWN:
                player_speed2+=2
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                player_speed2+=2
            elif event.key==pygame.K_DOWN:
                player_speed2-=2


        if event.type==pygame.QUIT:
            running=False
    player.y += player_speed
    bot.y += player_speed2
    screen.fill((0,0,0))
    dfs()
    dfs2()
    dfs1()
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.draw.rect(screen, (255, 255, 255), bot)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    txt.render_to(screen, (750, 10), str(scor[0]) + ":" + str(scor[1]), (255, 255, 255))
    pygame.display.flip()
    clock.tick(200)