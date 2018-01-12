import pygame

# Window.
window = pygame.display.set_mode((400, 435))
pygame.display.set_caption('Game')

# Holst.
screen = pygame.Surface((400, 400))

# Status bar.
info_string = pygame.Surface((400, 35))


class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((0, 0, 0))

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))


def intersect(x1, x2, y1, y2, db1, db2):
    if ((x1 > x2 - db1) and (x1 < x2 + db2)
            and (y1 > y2 - db1) and (y1 < y2 + db2)):
        return 1
    return 0


# Fonts.
pygame.font.init()
speed_font = pygame.font.SysFont('Comic Sans MS', 25, True, True)
info_font = pygame.font.SysFont('Comic Sans MS', 25, True, True)
lable_font = pygame.font.SysFont('ALGERIAN', 25, True, True)

# Hero and zet creating.
hero = Sprite(200, 350, 'images/h.png')
zet = Sprite(10, 10, 'images/z.png')
zet.right = False
zet.step = 1

arrow = Sprite(-40, 350, 'images/arrow.png')
arrow.push = False

done = True
pygame.key.set_repeat(1, 1)
score = 0
lable_color = 255

while done:
    # Main game loop.
    for e in pygame.event.get():
        if e.type is pygame.QUIT:
            done = False

        # Manipulations with hero.
        # Key motions.
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                if hero.x > 10:
                    hero.x -= 1
            if e.key == pygame.K_RIGHT:
                if hero.x < 350:
                    hero.x += 1
            if e.key == pygame.K_UP:
                if hero.y > 200:
                    hero.y -= 1
            if e.key == pygame.K_DOWN:
                if hero.y < 350:
                    hero.y += 1

            # Arrow activation.
            if e.key == pygame.K_SPACE:
                if arrow.push == False:
                    arrow.x = hero.x + 5
                    arrow.y = hero.y
                    arrow.push = True

        # Mouse motions.
        if e.type == pygame.MOUSEMOTION:
            pygame.mouse.set_visible(False)
            coord = pygame.mouse.get_pos()
            if coord[0] in range(10, 350):
                hero.x = coord[0]
            if coord[1] in range(200, 350):
                hero.y = coord[1]

                

        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                if arrow.push == False:
                    arrow.x = hero.x + 5
                    arrow.y = hero.y
                    arrow.push = True

    # Pouring
    screen.fill((50, 50, 50))
    info_string.fill((45, 80, 40))

    # Change title color.
    lable_color += 0.1
    if lable_color > 255:
        lable_color = 100

    # Zet moves.
    if zet.right == True:
        zet.x -= zet.step
        if zet.x < 0:
            zet.right = False
    else:
        zet.x += zet.step
        if zet.x > 360:
            zet.right = True

    # Arrow moves.
    if arrow.y < 0:
        arrow.push = False

    if arrow.push == False:
        arrow.y = 350
        arrow.x = -40

    else:
        arrow.y -= 2

    if intersect(arrow.x, zet.x, arrow.y, zet.y, 40, 40):
        arrow.push = False
        zet.step += 0.2
        score += 1

    # Fonts rendering.
    info_string.blit(info_font.render('Score: ' + str(score), 1,
                                      (210, 120, 200)), (10, 0))
    info_string.blit(lable_font.render('{SHOT}', 1, (0, lable_color, 0)), (150, 5))

    info_string.blit(speed_font.render('Spd: ' + str(round(zet.step, 1)), 1,
                                       (210, 120, 200)), (280, 0))

    # Show holst on screen.

    # Objects rendering.
    zet.render()
    hero.render()
    arrow.render()
    window.blit(info_string, (0, 0))
    window.blit(screen, (0, 35))
    pygame.time.delay(7)
    pygame.display.flip()
