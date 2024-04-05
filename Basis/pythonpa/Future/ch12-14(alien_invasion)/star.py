import pygame

from pygame.sprite import Sprite

class Star(Sprite):
	"""表示星星的类"""
	def __init__(self,s_settings,screen):
		#初始化星星并设置其初始位置
		super(Star,self).__init__()
		self.screen = screen
		self.s_settings = s_settings
		
		#导入星星的图像
		self.image = pygame.image.load('images/星星.bmp')
		self.rect = self.image.get_rect()
		
		#每个星星最初都在屏幕左上角
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#存储星星的准确位置
		self.x = float(self.rect.x)
		
	def blitme(self):
		"""在指定位置绘制星星"""
		self.screen.blit = (self.image,self.rect)
	
