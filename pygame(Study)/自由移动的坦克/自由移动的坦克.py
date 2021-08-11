# coding=utf-8
import pygame
from pygame.locals import *
import sys
def play_tank():
    pygame.init()
    windows_size = (width,height) = (600,400)  # 窗口大小
    speed = [1,1]  # 运动偏移量；值越大，移动越快
    color_blank = (255,255,255)  # 窗口背景RGB值（白色）
    screen = pygame.display.set_mode(windows_size)  # 设置窗口模式
    pygame.display.set_caption('自由移动的坦克')  # 设置窗口标题
    tank_image = pygame.image.load('tankU.bmp')  # 加载坦克图片，返回一个surface对象

    tank_rect = tank_image.get_rect()  # 获取坦克图片的区域形状
    while True:  # 无限循环
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 退出事件处理
                pygame.quit()
                sys.exit()
        # 使坦克移动，速度由speed变量控制
        tank_rect = tank_rect.move(speed)
        if (tank_rect.left < 0) or (tank_rect.right > width):  # 水平方向
            speed[0] = -speed[0]  # 水平方向反向
        if (tank_rect.top < 0) or (tank_rect.bottom > height):  # 垂直方向
            speed[1] = -speed[1]  # 垂直方向反向
        screen.fill(color_blank)  # 填充窗口背景
        screen.blit(tank_image, tank_rect)  # 在窗口指定区域tank_rect上绘制坦克
        pygame.display.update()  # 更新窗口显示内容
if __name__ == '__main__':
    play_tank()