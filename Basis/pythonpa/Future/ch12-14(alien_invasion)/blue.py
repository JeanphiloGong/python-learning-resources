#创建一个背景为蓝色的pygame窗口
import pygame
import sys
from character import Character

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption('blue display ')
	
	
	#设置背景色
	bg_color = (0,0,230)
	
	#创建一个角色
	character = Character(screen)
	
	
	#开始主循环
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
		
		#更新屏幕图像
		screen.fill(bg_color)
		character.blitme()
		
		
		#让最近绘制的屏幕可见
		pygame.display.flip()
		
run_game()

