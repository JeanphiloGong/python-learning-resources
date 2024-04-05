#测试ship中center的数值类型的简单测试
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

#创建一个ai——settings对象
ai_settings = Settings()
#创建一个screen对象
screen = pygame.display.set_mode(
	    (ai_settings.screen_width, ai_settings.screen_height))

ship = Ship(ai_settings,screen)

print(type(ship.center))
print(type(ai_settings.ship_speed_factor))
