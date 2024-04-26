import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (255, 255, 255)

BALL_RADIUS = 20
BALL_COLOR = (255, 0, 0)

PLAYER_WIDTH = 100
PLAYER_HEIGHT = 20
PLAYER_COLOR = (0, 0, 255)

FPS = 60

def draw_ball(screen, x, y):
    pygame.draw.circle(screen, BALL_COLOR, (x, y), BALL_RADIUS)

def draw_player(screen, x, y):
    pygame.draw.rect(screen, PLAYER_COLOR, (x, y, PLAYER_WIDTH, PLAYER_HEIGHT))

def main():
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pygame Game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    player_x -= 5
if keys[pygame.K_RIGHT]:
    player_x += 5

ball_x += ball_speed_x
ball_y += ball_speed_y

if ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= SCREEN_WIDTH:
    ball_speed_x = -ball_speed_x
if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= SCREEN_HEIGHT:
if ball_y + BALL_RADIUS >= player_y and ball_x >= player_x and ball_x <= player_x +
   ball_speed_y = -ball_speed_y
screen.fill(BG_COLOR)
