import pygame

import screen_function as sf
from screen_settings import Settings
from pygame.sprite import Group

def run():
	#创建一个屏幕并初始化游戏对象
	pygame.init()
	s_settings = Settings()
	screen = pygame.display.set_mode((s_settings.screen_width,s_settings.screen_height))
	#为窗口命名
	pygame.display.set_caption('Star')
	stars = Group()
	#创建星星群
	sf.create_fleet(s_settings,screen,stars)
	print(len(stars))
	
	while True:
		#响应按键
		sf.check_events(screen)
		#填充背景加载星星
		sf.update_screen(s_settings,screen,stars)
		


run()
	
	
	

