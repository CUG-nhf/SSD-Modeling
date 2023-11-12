import pygame
import sys

# 初始化pygame
pygame.init()

# 设置窗口大小
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("坐标系示例")

# 定义颜色
white = (255, 255, 255)

# 加载图片
image_path = "picture/pic2.png"  # 将路径替换为你的图片路径
image = pygame.image.load(image_path)
image = pygame.transform.scale(image, (width, height))

# 渲染图片到窗口
screen.blit(image, (0, 0))

# 更新显示
pygame.display.flip()

def convert_coordinates(mouse_pos):
    # 将鼠标点击的窗口坐标转换为直角坐标系中的坐标
    x = mouse_pos[0]
    y = height - mouse_pos[1]  # 将窗口坐标系转换为直角坐标系
    return x, y

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 检测鼠标左键点击
                mouse_position = pygame.mouse.get_pos()
                coordinates = convert_coordinates(mouse_position)
                print("鼠标点击坐标:", coordinates)

    pygame.display.update()
