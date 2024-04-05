import pygame

from pygame.sprite import Sprite

class Raindrops(Sprite):
	"""表示单个外星人的类"""
	
	def __init__(self,ed_settings,screen):
		"""初始化外星人并设置其起始位置"""
		super(Raindrops,self).__init__()
		self.screen = screen
		self.ed_settings = ed_settings
		
		#加载外星人图像并设置其rect属性
		self.image = pygame.image.load('images/雨滴.bmp')
		self.rect = self.image.get_rect()
		
		#每个外星人最初都在屏幕左上角辅警
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#存储外星人的准确位置
		self.y = float(self.rect.y)
		
	
	def blitme(self):
		"""在指定位置绘制外星人"""
		self.screen.blit(self.image,self.rect)
		
	
	def check_bottom(self):
		"""如果雨滴下降到屏幕之外就返回True"""
		screen_rect = self.screen.get_rect()
		if self.rect.top >= screen_rect.bottom:
			return True

