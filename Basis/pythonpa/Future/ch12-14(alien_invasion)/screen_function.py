import pygame

import sys
from star import Star
from random import randint

#存储screen中需要的一些函数


def check_events(screen):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()


def update_screen(s_settings,screen,stars):
	#重绘屏幕
	screen.fill(s_settings.bg_color)
	stars.draw(screen)
	#绘制屏幕
	pygame.display.flip()
		
	
def create_fleet(s_settings,screen,stars):
	#创建一个外星人
	star = Star(s_settings,screen)
	number_star_x = get_number_star_x(s_settings,star.rect.width)
	number_rows = get_number_rows(s_settings,star.rect.height)
	print(type(number_rows))
	#创建星星群
	for row_number in range(randint(0,number_rows),randint(0,number_rows)):
		for star_number in range(randint(0,number_rows),randint(0,number_star_x)):
			create_star(s_settings,screen,stars,star_number,row_number)
	
	
	
def get_number_star_x(s_settings,star_width):
	"""计算一行可以容纳多少星星"""
	available_space_x = s_settings.screen_width - (2 * star_width)
	number_star_x = int(available_space_x / (2 * star_width))
	return number_star_x
	

def get_number_rows(s_settings,star_height):
	"""计算屏幕可以容纳多少外星人"""
	available_space_y = s_settings.screen_height - (3 * star_height)
	number_rows = int(available_space_y / (2 * star_height))
	return number_rows
	
	
def create_star(s_settings,screen,stars,star_number,row_number):
	"""创建一个外星人并将其放置在当前行"""
	star = Star(s_settings,screen)
	star_width = star.rect.width
	star.x = star_width + 2 * star_width * star_number
	star.rect.x = star.x
	star.rect.y = star.rect.height + 2* star.rect.height * row_number
	stars.add(star)
