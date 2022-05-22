import pygame
from sys import exit

pygame.init()
font = pygame.font.SysFont('Roboto', 60)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

player_score = 0
enemy_score = 0

move_speed = 5
player = pygame.Rect(10, 240, 20, 60)
enemy = pygame.Rect(770, 240, 20, 60)
ball = pygame.Rect(400, 300, 20, 20)

ball_move_y = 3
ball_move_x = 3

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player.y > 0:
        player.y -= move_speed
    if keys[pygame.K_s] and player.y < 540:
        player.y += move_speed
    if keys[pygame.K_UP] and enemy.y > 0:
        enemy.y -= move_speed
    if keys[pygame.K_DOWN] and enemy.y < 540:
        enemy.y += move_speed

    screen.fill((0, 0, 0))

    player_text = font.render(f'{player_score}', True, (255, 255, 255))
    enemy_text = font.render(f'{enemy_score}', True, (255, 255, 255))
    screen.blit(player_text, (200, 20))
    screen.blit(enemy_text, (600, 20))

    player = pygame.draw.rect(screen, (255, 255, 255), player)
    enemy = pygame.draw.rect(screen, (255, 255, 255), enemy)
    ball = pygame.draw.rect(screen, (255, 255, 255), ball)

    ball.y += ball_move_y
    ball.x += ball_move_x

    if ball.top <= 0 or ball.bottom >= 600:
        ball_move_y *= -1
    if ball.left <= 0:
        enemy_score += 1
        ball_move_x *= -1
        ball.center = (400, 300)
    if ball.right >= 800:
        player_score += 1
        ball_move_x *= 1
        ball.center = (400, 300)
    if ball.colliderect(player) or ball.colliderect(enemy):
        ball_move_x *= -1

    clock.tick(60)
    pygame.display.update()
