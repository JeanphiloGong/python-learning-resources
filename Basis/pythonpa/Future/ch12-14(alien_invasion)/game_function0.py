import sys 

import pygame
from bullet0 import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	"""响应按键"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
		
def fire_bullet(ai_settings,screen,ship,bullets):
	"""如果没有达到限制，就发射一颗子弹"""
	#创建薪子弹，并将其加入到编组bullets中
	if len(bullets) < ai_settings.bullet_allowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)


def check_keyup_events(event,ship):
	"""响应松开"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False



def check_event(ai_settings,screen,ship,bullets):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
			


def update_screen(ai_settings,screen,ship,bullets):
	"""在每次操作时都刷新屏幕图像"""
	#每次循环的时候都刷新屏幕
	screen.fill(ai_settings.bg_color)
	#在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	
	#让最近绘制的屏幕可见
	pygame.display.flip()
	
def update_bullets(bullets,ai_settings):
	"""更新子弹的位置，并删除已经消失的子弹"""
	#更新子弹的位置
	bullets.update()
	
	#删除已经消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.right >= 1200 :
			bullets.remove(bullet)
		

