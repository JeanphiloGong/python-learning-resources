import sys

import pygame

def check_events():
	"""响应键盘和鼠标事件"""
	#创建窗口退出按钮
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
def update_screen(c_settings,screen):
	"""对屏幕画面进行更新"""
	#填充颜色
	
	#重绘刚刚绘制的屏幕
	
	
