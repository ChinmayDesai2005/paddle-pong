import pygame
import game
import sys
import random
pygame.init()
window = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Ping Pong")
window.fill((0, 0, 0))
font_all = "8-BIT WONDER.ttf"
GameOn = True
MainGame = True
vel = 10
velx = 8
vely = 3
left = 250
right = 250
ball_x = 350
ball_y = 300
s1 = 0
s2 = 0
clock = pygame.time.Clock()


def random_start():
    global ball_x, ball_y
    global start_random
    ball_x = 350
    ball_y = 350
    ball_start = ["left_startup", "right_startup", "left_startdown", "right_startdown"]
    start_random = random.choice(ball_start)
    #print(start_random)


class DrawThings:
    def __init__(self):
        self.surface = window
        self.width = 25
        self.height = 125
        self.color = (255, 255, 255)

    def make_box(self, x, y):
        self.x = x
        self.y = y
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.width, self.height))

    def make_ball(self, x_ball, y_ball):
        self.x_ball = x_ball
        self.y_ball = y_ball
        self.radius = 10
        pygame.draw.circle(self.surface, self.color, (self.x_ball, self.y_ball), self.radius)


def wall_crash():
    global ball_x, ball_y, s1, s2
    if ball_x < 0:
        ball_x = 350
        ball_y = 300
        s2 += 1
        random_start()
    if ball_x > 700:
        ball_x = 350
        ball_y = 300
        s1 += 1
        random_start()


random_start()


def main_game():
    global left, right, ball_x, ball_y, velx, vely, MainGame, clock
    global start_random, GameOn
    #clock.tick(60)
    box_left = DrawThings()
    box_left.make_box(15, left)
    box_right = DrawThings()
    box_right.make_box(660, right)
    ball = DrawThings()
    # Misc For Testing
    ball.make_ball(ball_x, ball_y)
    # Key Presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left > 10:
        left -= vel
    elif keys[pygame.K_s] and left < 465:
        left += vel
    # Random Start Directions
    if start_random == "right_startup":
        ball_x += velx
        ball_y -= vely
    elif start_random == "left_startup":
        ball_x -= velx
        ball_y -= vely
    elif start_random == "left_startdown":
        ball_x -= velx
        ball_y += vely
    elif start_random == "right_startdown":
        ball_x += velx
        ball_y += vely

    # Movement
    if keys[pygame.K_UP] and right > 10:
        right -= vel
    elif keys[pygame.K_DOWN] and right < 465:
        right += vel

    # Collision with walls
    wall_crash()
    # Collision with Bars
    if ball_x < 40 and ball_x > 15 and ball_y < (left + 125) and ball_y > left:
        velx = -1 * velx

    elif ball_x > 640 and ball_x > 665 and ball_y < (right + 125) and ball_y > right:
        velx = -1 * velx

    else:
        wall_crash()

    # Reflection of ball from up and down wall
    if ball_y < 0:
        vely = -1 * vely
    elif ball_y > 580:
        vely = -1 * vely
    score = "    Player 1 = " + str(s1) + "                        Player 2 = " + str(s2)
    font = pygame.font.Font(font_all, 20)
    text = font.render(score, True, (255, 255, 255))
    window.blit(text, (0, 10))
    if s1 == 10:
        text_end = font_end.render("Player 1 Won!!", True, (0, 0, 0), (255, 225, 225))
        window.blit(text_end, (270, 260))
        GameOn = False
        self.game.main_running = True
    elif s2 == 10:
        text_end = font_end.render("Player 2 Won!!", True, (0, 0, 0), (255, 225, 225))
        window.blit(text_end, (230, 270))
        GameOn = False
        self.game.main_running = True
    pygame.display.update()
    window.fill((0, 0, 0,))
    # sys exit
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


while GameOn:
    clock.tick(60)
    main_game()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

pygame.quit()