#和飞船相关的类
import pygame

class Ship():
	def __init__(self,ai_settings,screen):
		self.screen = screen
		self.ai_settings = ai_settings
		
		#加载飞船图像并获取其外接矩形
		self.image = pygame.image.load("images/狐狸书生.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		
		#将飞创放置在屏幕中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom/2
		
		#飞船属性中存储小数值
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
		#移动标志，使得飞船可以不断移动
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
	
	def update(self):
		"""根据移动标志调整飞船的位置"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0 :
			self.centerx  -= self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centery  += self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.top > 0:
			self.centery  -= self.ai_settings.ship_speed_factor
			
		#根据self.centerx/y更新rect对象
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
		
		
		
	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image,self.rect)



