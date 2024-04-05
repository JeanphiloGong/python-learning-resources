import pygame
#存储外星人入侵的相关设置
class Settings():
	#屏幕属性的相关设置，窗口大小和窗口的背景颜色
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		
		#限制飞船的移动速度
		self.ship_speed_factor = 1.5
		
		#添加子弹设置
		self.bullet_speed_factor = 1
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color =60,60,60
		self.bullet_allowed = 100
		
		



