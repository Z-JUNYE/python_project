import sys # 玩家退出时，使用sys模块中的工具来退出游戏。
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))  # 创建一个显示窗口，赋给self.screen，让类的所有方法都能使用它
        # 赋给self.screen的对象是一个surface。 在pygame中，surface是屏幕的一部分，用于显示游戏元素。
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
    
    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            # 侦听键盘和鼠标事件
            for event in pygame.event.get(): # 事件是用户玩游戏时执行的操作，如案件或移动鼠标。为了让程序能够响应事件，可编写一个事件循环。
                if event.type == pygame.QUIT: #捕捉到窗口关闭按钮，将检测到QUIT事件
                    sys.exit()
            
            #每次循环时都会重绘屏幕
            self.screen.fill(self.settings.bg_color)

            self.ship.blitme()

            # 让最近绘制的屏幕可见
            pygame.display.flip()
            self.clock.tick(60) # tick方法接受一个参数：游戏的帧率，pygame将尽可能确保这个循环每秒运行60次。

if __name__ == "__main__":
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()