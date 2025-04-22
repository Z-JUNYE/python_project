import pygame

class Ship:
    '''管理飞船的类'''
    def __init__(self,ai_game): # 第二个参数是alienInvasion实例
        '''初始化飞船并设置其初始位置'''
        self.screen = ai_game.screen  # 将屏幕赋给ship的一个属性
        self.screen_rect = ai_game.screen.get_rect() # 访问屏幕的rect属性，以便能将飞船放到正确的位置
    
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('alien_invasion/images/ship.bmp') # 飞船图像的位置传递给一个surface。
        self.rect = self.image.get_rect() # 获取相应的surface的属性rect

        # 每艘新飞船都放在屏幕底部中间
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect) # 将图像绘制到self.rect指定的位置
