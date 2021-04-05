import pygame

pygame.init()

xy = 800
win = pygame.display.set_mode((xy, xy))
pygame.display.set_caption("Bounce!")
run = True
clock = pygame.time.Clock()
Frame = 0
shadows = []


class Bouncer:
    def __init__(self, color):
        self.color = color
        self.x = xy // 2
        self.y = xy // 2
        self.wh = 30
        self.xvel = 0
        self.yvel = 0
        self.rect = (self.x, self.y, self.wh, self.wh)
        for s in range(60):
            shadows.append(self.rect)

    def draw(self):
        self.update()
        grey = [255, 255, 255]
        for s in shadows:
            pygame.draw.rect(win, grey, s)
            grey[1] -= 4
            grey[2] -= 4
        pygame.draw.rect(win, self.color, self.rect)

    def update(self):
        global shadows
        self.rect = (self.x, self.y, self.wh, self.wh)
        del shadows[0]
        shadows.append(self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        # BOUNCING
        if self.y < 0:  # TOP
            self.y = 0
            self.yvel = - 0.8 * self.yvel
            print("hit TOP")
        if self.y > xy - self.wh:  # BOTTOM
            self.y = xy - self.wh
            self.yvel = - 0.8 * self.yvel
            print("hit BOTTOM")
        if self.x + self.xvel > xy - self.wh:  # RIGHT
            self.x = xy - self.wh
            self.xvel = - 0.8 * self.xvel
            print("hit RIGHT")
        if self.x < 0:  # LEFT
            self.x = 0
            self.xvel = - 0.8 * self.xvel
            print("hit LEFT")
        # ACCELERATION
        if keys[pygame.K_w]:
            print("moved up")
            self.yvel -= 0.05
        if keys[pygame.K_s]:
            print("moved down")
            self.yvel += 0.05
        if keys[pygame.K_d]:
            print("moved right")
            self.xvel += 0.05
        if keys[pygame.K_a]:
            print("moved left")
            self.xvel -= 0.05
        # MOVING
        self.y += self.yvel
        self.x += self.xvel


bouncer = Bouncer((255,165,0))


def redrawWin():
    global Frame
    win.fill((255, 255, 255))
    bouncer.draw()
    bouncer.move()
    pygame.display.update()
    Frame += 1


def main():
    global run
    while run:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        if run:
            print("Frame Nr. ", Frame)
            print(shadows)
            redrawWin()


main()
