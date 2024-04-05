#外星人入侵的练习
import pygame
from pygame.sprite import Group

import sys
from settings0 import Settings
import game_function0 as gf
from ship0 import Ship


def run_game():
	#初始化游戏并创造一个屏幕对象 初始化pygame、设置和屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	 (ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien_Invasion0")
	
	#创建一艘飞船
	ship = Ship(ai_settings,screen)
	#创建一个用于存储子弹的编组
	bullets = Group()
	test =[ai_settings.screen_width ]
	if test:
		print(test)
	
	#开始游戏的主循环
	while True:
		#显示键盘和鼠标事件
		gf.check_event(ai_settings,screen,ship,bullets)
		#使得飞船可以不断移动
		ship.update()
		bullets.update()
		#删除已经消失的子弹
		gf.update_bullets(bullets,ai_settings)
		
		#更新屏幕和图像
		gf.update_screen(ai_settings,screen,ship,bullets)
		print(len(bullets))
	
		
		
		
		

		

	
run_game()


