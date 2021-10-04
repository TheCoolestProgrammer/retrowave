import pygame

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))

#palm = pygame.image.load("palm.png")
#palm2 = pygame.image.load("palm2.png")

speed = 2
road_width = 10
#x = (screen_width // 2) + (road_width//2)

#y = (screen_height // 2) - palm_height

sun = pygame.image.load("sun.png")
palms = []
amount_palms =45

x2 = (screen_width // 2) - (road_width//2) -23
y2 = (screen_height // 2) - (screen_height // (screen_width // speed)) -50

streight = 1
class Palm:
    palm_height = screen_height // (screen_width // speed)
    palm_width = (palm_height // 2)
    x = (screen_width // 2) + (road_width//2)
    y = (screen_height // 2) - palm_height
    palm = pygame.image.load("palm.png")
    palm2 = pygame.image.load("palm2.png")
    palm = pygame.transform.scale(palm, (palm_width, palm_height))
    palm2 = pygame.transform.scale(palm2, (palm_width, palm_height))

# i = (screen_width // 2) + (road_width//2)
# r = (screen_height // 2) - (screen_height // (screen_width // speed))
# while i < 0:
#     i -= speed
#     r += speed
# line1_x = r
# line1_y = i

# i = (screen_width // 2) - (road_width//2)
# r = (screen_height // 2) - (screen_height // (screen_width // speed))
# while r < screen_height:
#     i -= speed
#     r += speed
# line2_x = i
# line2_y = r

count = 0
while True:
    count += 1
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        if event.type == pygame.QUIT:
            pygame.quit()


    screen.fill((0, 0, 0))

    if count % amount_palms == 0 or count == 1:
    # if len(palms) <amount_palms:
    #     for i in range(amount_palms-len(palms)):

        a = Palm()
        palms.append(a)
    screen.blit(sun, (x2, y2))
    for i in range(len(palms)-1,-1, -1):
        if palms[i].x > screen_width:
            del(palms[i])
            continue
        screen.blit(palms[i].palm, (palms[i].x,palms[i].y))
        r = (screen_width//2) -(palms[i].x -(screen_width//2))-palms[i].palm_width
        screen.blit(palms[i].palm2,(r,palms[i].y))

        palms[i].palm_width += speed*2
        palms[i].palm_height += speed*2

        palms[i].palm = pygame.image.load("palm.png")
        palms[i].palm2 = pygame.image.load("palm2.png")
        palms[i].palm = pygame.transform.scale(palms[i].palm, (palms[i].palm_width, palms[i].palm_height))
        palms[i].palm2 = pygame.transform.scale(palms[i].palm2, (palms[i].palm_width, palms[i].palm_height))
        palms[i].x+=speed
        palms[i].y-=speed
        # if palms[i].y > (screen_height // 6) * 5:
        #     streight = 8
        # elif palms[i].y > (screen_height//4)*3:
        #     streight = 4
        # elif palms[i].y > (screen_height//3)*2:
        #     streight = 2
        # else:
        #     streight = 1
        #pygame.draw.line(screen, (224,99,255), (palms[i].x + (palms[i].palm_width // 3), palms[i].y + palms[i].palm_height), (r + (palms[i].palm_width//3*2), palms[i].y + palms[i].palm_height),8)
        pygame.draw.line(screen, (224,99,255), (0, palms[i].y + palms[i].palm_height), (screen_width, palms[i].y + palms[i].palm_height),streight)
        pygame.draw.line(screen, (224,99,255), (0, screen_height//2 +5), (screen_width, screen_height//2+5), streight)
        pygame.draw.line(screen, (224, 99, 255),(screen_width-140, screen_height),(x2+50, y2+55),streight)
        pygame.draw.line(screen, (224, 99, 255), (140, screen_height), (x2+10,y2+55), streight)
        pygame.draw.line(screen, (224, 99, 255),(screen_width-280, screen_height),(x2+35, y2+55),streight)
        pygame.draw.line(screen, (224, 99, 255), (280, screen_height), (x2+20,y2+55),streight)

        pygame.draw.line(screen, (224, 99, 255),(screen_width-420, screen_height),(x2+25, y2+55),streight)
        pygame.draw.line(screen, (224, 99, 255), (420, screen_height), (x2+30,y2+55), streight)
        pygame.draw.line(screen, (224, 99, 255), (screen_width-560, screen_height),(x2+24, y2+55), streight)
        pygame.draw.line(screen, (224,99,255), (560, screen_height),(x2+25, y2+55),streight)
    pygame.display.update()
