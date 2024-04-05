import pygame

class Character():
	""""创建一个图像并将其放置在窗口的中心位置"""
	
	def __init__(self,screen):
		self.screen = screen
		
		#加载角色并获取其外接矩形
		self.image = pygame.image.load('images/狐狸书生.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		
		#将角色放置在屏幕底部
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
	
	def blitme(self):
		#绘制角色
		self.screen.blit(self.image,self.rect)
		

