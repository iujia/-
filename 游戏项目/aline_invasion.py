import sys

import pygame

def run_game():
    pygame.init()
    screen=pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    #开始游戏的主循环
    while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                  sys.exit()
                   #让最近绘制的屏幕可见
                  pygame.display.flip()
            
                    
run_game()
