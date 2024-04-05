import pygame

from c_settings import Settings
import crash_functions as cf

def run():
	#初始化游戏并创建一个屏幕
	pygame.init()
	c_settings = Settings()
	#设置窗口大小
	screen = pygame.display.set_mode = (
	    (c_settings.screen_width,c_settings.screen_height))
	#设置窗口名称
	pygame.display.set_caption('BALL_CRASH')
	
	#开始游戏循环
	while True:
		cf.check_events()
		pygame.display.flip()

		
		
run()
		
	
