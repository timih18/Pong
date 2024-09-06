import pygame
from ball import Ball
from paddle import Paddle
from target import Target


pygame.init()

background_color = (18, 116, 201)
main_color = (255, 255, 255)

size = (500, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pong 2')

ball = Ball(main_color, 10, 10)
ball.rect.x = 195
ball.rect.y = 345

paddle = Paddle(main_color, 100, 10)
paddle.rect.x = 200
paddle.rect.y = 675

target = Target(main_color, 50, 5)
target.rect.x = 225
target.rect.y = 0

sprites = pygame.sprite.Group()
sprites.add(ball)
sprites.add(paddle)
sprites.add(target)

on = True
game_over = False
clock = pygame.time.Clock()
score = 0

while on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        paddle.move_left(5)
    if keys[pygame.K_d]:
        paddle.move_right(5)

    sprites.update()

    if ball.rect.x > 490:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x < 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y >= 690:
        on = False
        game_over = True
    if ball.rect.y <= 0:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddle):
        ball.bounce()
    if pygame.sprite.collide_mask(ball, target):
        ball.bounce()
        score += 1
    
    screen.fill(background_color)
    sprites.draw(screen)

    font = pygame.font.Font(None, 74)
    text = font.render(str(score), 1, main_color)
    screen.blit(text, (15, 15))

    pygame.display.flip()
    clock.tick(60)

on = True 

if game_over:
    while on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False

        screen.fill(background_color)
        font = pygame.font.Font(None, 90)
        text = font.render('GAME OVER!', 1, main_color)
        screen.blit(text, (53, 300))
        font = pygame.font.Font(None, 45)
        text = font.render(f'Score: {score}', 1, main_color)
        screen.blit(text, (180, 370))

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
