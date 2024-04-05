import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""一个对飞船发射的子弹进行管理的类"""
	
	def __init__(self,ai_settings,screen,ship):
		"""在飞船所处的位置创建一个子弹对象"""
		super(Bullet,self).__init__()
		self.screen = screen
		
		#在(0,0)位置创建一个表示子弹的矩形，再设置正确的位置
		self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
		     ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.right = ship.rect.right
		self.rect.top = (ship.rect.top + ship.rect.bottom)/2
		
		
		#存储用小数表示的子弹位置
		self.centerx = float(self.rect.centerx)
		
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
		
	def update(self):
		"""向右移动子弹"""
		#更新表示子弹位置的小数值
		self.centerx += self.speed_factor
		#更新表示子弹的rectangle的位置
		self.rect.centerx = self.centerx
		
	def draw_bullet(self):
		"""在屏幕上绘制子弹"""
		pygame.draw.rect(self.screen,self.color,self.rect)

