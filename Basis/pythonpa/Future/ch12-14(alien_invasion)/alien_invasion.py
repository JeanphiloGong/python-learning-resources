import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

def run_game():
	#初始化游戏并创建一个屏幕对象  初始化pygame、设置和屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	    (ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien_Invasion")
	#创建Play按钮
	play_button = Button(ai_settings,screen,"Play")
	#创建一个用于存储游戏统计信息的实例,并创建记分牌
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	#创建一艘飞船和存储子弹和外星人的编组
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()
	#创建外星人群
	gf.create_fleet(ai_settings,screen,ship,aliens)
	#开始游戏的主循环
	while True:
		#显示键盘和鼠标事件
		gf.check_events(ai_settings,screen,stats,sb,play_button,
		    ship,aliens,bullets)
		if stats.game_active:
			#使得飞船可以不断移动
			ship.update()
			#移动子弹
			bullets.update()
			#删除已经消失的子弹
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			#更新外星人位置
			gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)
			
		#让最近绘制的屏幕可见
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
		
		
run_game()
		
	

	


