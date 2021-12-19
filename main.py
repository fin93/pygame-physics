import math     # importing libraries
import pygame

pygame.init()

WIDTH, HEIGHT = 600, 600
FPS = 60
BG_COLOUR = (217, 217, 217)

move_right = False
move_left = False
g = 10
vel = 0
jmp_height = -1
x, y = 300, 30
x_vel = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("clean")
CLOCK = pygame.time.Clock()
screen.fill(BG_COLOUR)


def draw_circle(x_, y_):
    pygame.draw.circle(screen, (100, 100, 100), (x_, y_), 10)   # drawing the sprite at x and y co-ords


draw_circle(x, y)
pygame.display.update()


def jump():
    global vel
    vel = -1 * math.sqrt(jmp_height * -2 * g)   # the formula for jumping


def x_move(k_pressed, a):   # if left or right is pressed/held down
    global x_vel
    if k_pressed and a == 0:
        x_vel += g * 0.01
    if k_pressed and a == 1:
        x_vel -= g * 0.01


def friction(x_v):  # friction
    global x_vel
    if x_v > 0:
        x_vel -= 0.03

    elif x_v < 0:
        x_vel += 0.03


def hit_wall():   # reverses x-axis velocity if the ball hits a wall
    global x_vel
    x_vel *= -1


def bounce():   # if the ball hits the ground it bounces at 5/6 its reverse vel basically lazy physics
    global vel, y
    y = 599
    vel *= -1
    vel -= vel // 6


def tele(x_):   # if ball hits walls changes x-axis to opposite wall and keeps current velocity
    global x
    if x_ < 5:
        x = 599
    if x_ > 595:
        x = 1


while True:   # main loop
    CLOCK.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump()
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_q:
                pygame.quit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False

    vel += g * 0.02
    y += vel
    x += x_vel

    if not move_left or not move_right:
        friction(x_vel)

    if move_right:  # self-explanatory
        x_move(move_right, 0)
    if move_left:   # self-explanatory
        x_move(move_left, 1)
    if y >= 600:    # if the ball hits the floor
        bounce()
    """
    if x > 599 or x < 1:    # option of teleporting on walls comment this and uncomment the commented part for bounce
        tele(x)
    """
    if x >= 600 or x <= 0:  # option of bouncing back off walls
        hit_wall()
    
    screen.fill(BG_COLOUR)
    draw_circle(x, y)
    pygame.display.update()
