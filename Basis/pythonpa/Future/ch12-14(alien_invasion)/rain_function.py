import sys

import pygame
from raindrops import Raindrops
#存储rain_drop相关的一些函数

def update_screen(ed_settings,screen,raindrops):
	screen.fill(ed_settings.bg_color)
	raindrops.draw(screen)
	#让最近绘制的屏幕可见
	pygame.display.flip()
	
def check_event():
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

def create_fleet(ed_settings,screen,raindrops):
	"""创建雨滴群"""
	#创建一个雨滴
	raindrop = Raindrops(ed_settings,screen)
	number_raindrop_x = get_number_raindrop_x(ed_settings,raindrop.rect.width)
	number_rows = get_number_rows(ed_settings,raindrop.rect.height)
	#创建雨滴群
	for raindrop_number in range(number_raindrop_x):
		create_raindrop(ed_settings,screen,raindrops,raindrop_number)



	
def get_number_raindrop_x(ed_settings,raindrop_width):
	"""计算一行可以容纳多少雨滴"""
	available_space_x = ed_settings.screen_width - (2* raindrop_width)
	number_raindrop_x = int(available_space_x / (2* raindrop_width))
	return number_raindrop_x
	

def get_number_rows(ed_settings,raindrop_height):
	"""计算屏幕可以容纳多少雨滴"""
	available_space_y = (ed_settings.screen_height - (3 * raindrop_height)
	              - 300)
	number_rows = int(available_space_y / (2* raindrop_height))
	return number_rows
	
	
def create_raindrop(ed_settings,screen,raindrops,raindrop_number):
	"""创建一个外星人并将其放置在当前行"""
	raindrop = Raindrops(ed_settings,screen)
	raindrop_width = raindrop.rect.width
	raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
	raindrop.rect.x = raindrop.x
	raindrop.rect.y = raindrop.rect.height + 2 * raindrop.rect.height 
	raindrops.add(raindrop)
	

def check_fleet_bottom(ed_settings,raindrops,screen):
	"""有雨滴达到底部时再次召唤一批雨滴"""
	if len(raindrops)  <= 0:
		create_fleet(ed_settings,screen,raindrops)

		
def update_raindrops_location(ed_settings,raindrops):
	"""将整群雨滴向下移动"""
	for raindrop in raindrops.sprites():
		raindrop.rect.y += ed_settings.raindrop_speed_factor


def update_raindrops(ed_settings,raindrops,screen):
	"""移动雨滴位置并在雨滴到达底部时更新雨滴并删除已经消失的雨滴"""
	#将整群雨滴向下移动
	update_raindrops_location(ed_settings,raindrops)
	#有雨滴到达底部时再创造一批雨滴
	check_fleet_bottom(ed_settings,raindrops,screen)
	#删除已经消失的雨滴
	delete_raindrops(raindrops)


def delete_raindrops(raindrops):
	"""删除已经消失的雨滴"""
	for raindrop in raindrops.copy():
		if raindrop.rect.top >= 1200:
			raindrops.remove(raindrop)
