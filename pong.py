# импортируем pygame, ball и paddle
import pygame
from ball import Ball
from paddle import Paddle


# запустим pygame
pygame.init()

# определим черный и белый цвета в rgb
black = (0, 0, 0)
white = (255, 255, 255)

# создадим окно
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pong')

# создадим две ракетки
paddleA = Paddle(white, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(white, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

# создадим мяч
ball = Ball(white, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# создадим лист спрайтов и добавим в него мяч и ракетки
sprites_list = pygame.sprite.Group()
sprites_list.add(paddleA)
sprites_list.add(paddleB)
sprites_list.add(ball)

# создадим переменную которая будет отвечать за ссостояние окна (открыто/закрыто)
on = True

# создадим часы которые будут контролировать обновление экрана
clock = pygame.time.Clock()

# создадим счетчики
scoreA = 0
scoreB = 0

# создадим основной цикл игры
while on:
    # создадим условие закрытия окна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

    # зададим кнопки движения ракеток
    # игрок А - w/s
    # игрок B - UP/DOWN
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.move_up(5)
    if keys[pygame.K_s]:
        paddleA.move_down(5)
    if keys[pygame.K_UP]:
        paddleB.move_up(5)
    if keys[pygame.K_DOWN]:
        paddleB.move_down(5)

    sprites_list.update()

    # отскок от стен
    if ball.rect.x >= 690:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    # определение столкновений с ракетками
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    # создадим окно
    screen.fill(black)
    pygame.draw.line(screen, white, [349, 0], [349, 500], 5)
    sprites_list.draw(screen)
    # счетчики
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, white)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), 1, white)
    screen.blit(text, (420, 10))
    pygame.display.flip()

    # устоновим частоту обновления экрана
    clock.tick(60)

# выйдем из pygame
pygame.quit()
