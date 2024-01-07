import pygame
from time import sleep

pygame.init()
mw = pygame.display.set_mode((500, 500))
mw.fill((0, 100, 100))
clock = pygame.time.Clock()
clock.tick(40)
pygame.display.update()


class Hitbox():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = ((0, 100, 100))
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Lable(Hitbox):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


class Picture(Hitbox):
    def __init__(self, filemane, x=0, y=0, width=10, height=10):
        Hitbox.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filemane)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


ball = Picture("c:\\Users\\admin\\Desktop\\Visual Studio Code\\ball.png", 200, 200, 50, 50)
platform = Picture("c:\\Users\\admin\\Desktop\\Visual Studio Code\\platform.png", 240, 420, 100, 30)

game_over = False

start_x = 5
start_y = 5
count = 9
monsters = []


for j in range(3):
    y = start_y + (55 * j)
    x = start_x + (27.5 * j)
    for i in range(count):
        monstrs = Picture("c:\\Users\\admin\\Desktop\\Visual Studio Code\\monstr.png", x, y, 50, 50)
        monsters.append(monstrs)
        x += 55
    count -= 1

move_left = False
move_right =  False

dx = 1
dy = -1

while not game_over:
    ball.fill()
    platform.fill()

    ball.draw()
    platform.draw()

    pygame.display.update()

    ball.rect.x += dx
    ball.rect.y += dy
    if ball.rect.colliderect(platform.rect):
        dy *= -1

    if ball.rect.x > 450 or ball.rect.x < 0:
        dx *= -1

    if ball.rect.y < 0:
        dy *= -1

    if ball.rect.y > 450:
        time_text = Lable(158, 150, 50, 58)
        time_text.set_text("YOU LOSE", 60, (255, 0, 0))
        time_text.draw(0, 0)
        pygame.display.update()
        sleep(5)
        game_over = True


    if len(monsters) == 0:
        time_text = Lable(150,150,50,50)
        time_text.set_text("YOU WIN", 60, (0,200,0))
        time_text.draw(10,10)
        pygame.display.update()
        sleep(5)
        game_over = True


    for m in monsters:
        m.draw()
        if m.rect.colliderect(ball.rect):
            monsters.remove(m)
            m.fill()
            dy *= -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False




    if move_left:
        platform.rect.x -= 3
    if move_right:
        platform.rect.x += 3
        
    pygame.display.update()
    clock.tick(220) 