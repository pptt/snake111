import pygame
import random

# 初始化Pygame
pygame.init()

# 窗口尺寸和颜色
WIDTH, HEIGHT = 600, 400
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 创建窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇")

# 蛇的初始设置
snake = [[100, 100], [90, 100], [80, 100]]
direction = 'RIGHT'
food = [random.randrange(1, WIDTH // 10) * 10, random.randrange(1, HEIGHT // 10) * 10]
score = 0

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)

    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # 移动蛇
    head = snake[0].copy()
    if direction == 'UP':
        head[1] -= 10
    elif direction == 'DOWN':
        head[1] += 10
    elif direction == 'LEFT':
        head[0] -= 10
    elif direction == 'RIGHT':
        head[0] += 10

    # 检测碰撞
    if (head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT or
            head in snake):
        running = False

    snake.insert(0, head)

    # 吃食物检测
    if head == food:
        score += 1
        food = [random.randrange(1, WIDTH // 10) * 10,
                random.randrange(1, HEIGHT // 10) * 10]
    else:
        snake.pop()

    # 绘制元素
    for pos in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], 10, 10))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
print("游戏结束！得分:", score)