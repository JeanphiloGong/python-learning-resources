import pygame
from pygame.sprite import Group

from ed_settings import Settings
import rain_function as rf

def run():
	"""初始化屏幕和相关设置"""
	pygame.init()
	ed_settings = Settings()
	screen =  pygame.display.set_mode((ed_settings.screen_width,
	               ed_settings.screen_height))
	pygame.display.set_caption('RAINDROP')
	#创建雨滴编组
	raindrops = Group()
	#创建雨滴群
	rf.create_fleet(ed_settings,screen,raindrops)
	while True:
		rf.check_event()
		rf.update_screen(ed_settings,screen,raindrops)
		rf.update_raindrops(ed_settings,raindrops,screen)
		print(len(raindrops))

run()
	               
	
	
