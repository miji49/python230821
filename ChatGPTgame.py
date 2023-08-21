import pygame
import random

# 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("블록 깨기 게임")

# 색상
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# 패들 설정
paddle_width = 100
paddle_height = 10
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - paddle_height - 20
paddle_speed = 5

# 공 설정
ball_size = 20
ball_x = screen_width // 2
ball_y = paddle_y - ball_size
ball_speed_x = 3
ball_speed_y = -3

# 블록 설정
block_width = 80
block_height = 30
num_blocks = 5
blocks = []

for i in range(num_blocks):
    block = pygame.Rect(
        i * (block_width + 10) + 50,  # X 좌표
        50,                            # Y 좌표
        block_width,                   # 너비
        block_height                   # 높이
    )
    blocks.append(block)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT]:
        paddle_x += paddle_speed

    # 경계 체크
    if paddle_x < 0:
        paddle_x = 0
    elif paddle_x > screen_width - paddle_width:
        paddle_x = screen_width - paddle_width

    # 공 이동
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 공과 벽 충돌
    if ball_x <= 0 or ball_x >= screen_width - ball_size:
        ball_speed_x *= -1
    if ball_y <= 0:
        ball_speed_y *= -1

    # 공과 패들 충돌
    if ball_y >= paddle_y and paddle_x <= ball_x <= paddle_x + paddle_width:
        ball_speed_y *= -1

    # 공과 블록 충돌
    for block in blocks:
        if block.colliderect(pygame.Rect(ball_x, ball_y, ball_size, ball_size)):
            ball_speed_y *= -1
            blocks.remove(block)
            break

    # 화면 그리기
    screen.fill(white)
    pygame.draw.rect(screen, blue, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, red, (ball_x, ball_y, ball_size, ball_size))
    for block in blocks:
        pygame.draw.rect(screen, blue, block)
    pygame.display.flip()

    # 게임 속도 조절
    pygame.time.Clock().tick(60)

# 게임 종료
pygame.quit()
