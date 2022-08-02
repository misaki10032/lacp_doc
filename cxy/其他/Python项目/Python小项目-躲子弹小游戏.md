# Python小游戏

​		在python整个语言系统学完以后,我得知了Pygame这个扩展,发现相当的好用,所以在个人兴趣下写了小游戏(还没彻底写完)作为学习.

## 游戏整体设计

​	窗口大小:1200×600 

​	游戏基本内容:使用一个类似马里奥的小人,进行类似飞机大战形式的躲子弹游戏:

​	大致py文件分类:

​		box类:类似马里奥箱子那种,可以站立

​		bullet类:boss发射的子弹

​		hinder类:障碍物类,从屏幕的左右两边发射火球,击中后主角死亡

​		part类:主人公类

​		road类:地面类,(emmmmmm本来可以不要这个,不知道咋的就加上了)

​		boss类:就是boss类

​		game_function:储存游戏的主要判定函数等等

​		main_cycle:游戏主函数部分

​		setting类:储存游戏的设置等等

## 代码块

### main_cycle.py:

```python
from time import sleep
import pygame
from settings import Settings
from part import Part
from BOSS import BOSS
from road import Road
from box import Box
import game_function as gf
from pygame.sprite import Group
import datetime
def run():
    pygame.init()
    game_setting=Settings()
    screen = pygame.display.set_mode((game_setting.screen_width, game_setting.screen_height))
    pygame.display.set_caption("茄理奥")
    box = Box(game_setting, screen)
    road = Road(game_setting, screen)
    boss = BOSS(screen,game_setting)
    part = Part(game_setting, screen,box,road)
    hinders=Group()
    hinder1s = Group()
    bullets = Group()
    # dt = datetime.datetime.now()
    gf.create_fleet(game_setting, screen, hinders)
    gf.create_fleet1(game_setting, screen, hinder1s)
    gf.create_bullet(game_setting,screen,bullets,boss)
    # gf.create_bullet(game_setting,screen,bullets,boss)
    while True:
        # 监听
            gf.check_events(part)
            part.update()
            boss.update()
            hinders.update()
            hinder1s.update()
            bullets.update()
            for hinder in hinders.copy():
                if hinder.rect.bottom >550 or hinder.rect.top<0 or hinder.rect.left<0 or hinder.rect.right>1200:
                    hinders.remove(hinder)
                if len(hinders)<1:
                    hinders.remove(hinder)
                    gf.create_fleet(game_setting, screen, hinders)
            for hinder1 in hinder1s.copy():
                if hinder1.rect.bottom > 550 or hinder1.rect.top < 0 or hinder1.rect.left < 0 or hinder1.rect.right > 1500:
                    hinder1s.remove(hinder1)
                if len(hinder1s) < 1:
                    hinder1s.remove(hinder1)
                    gf.create_fleet1(game_setting, screen, hinder1s)
            for bullet in bullets.copy():
                if bullet.rect.bottom > 550 or bullet.rect.top < 0 or bullet.rect.left < 0 or bullet.rect.right > 1200:
                    bullets.remove(bullet)
                if len(bullets) < 5:
                    bullets.remove(bullet)
                    gf.create_bullet(game_setting, screen, bullets,boss)
            gf.update_screen(game_setting, screen, part,hinders,boss,bullets,road,box,hinder1s)
run()
```

### settings.py:

```python
#因为后面代码越写越乱,本来好多东西应该放在设置类里面,请大家别学习这种行为
import pygame
class Settings(object):
    """储存游戏中所有的设置类"""
    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height =600
        self.bg_img =pygame.image.load("image/backgroud.jpg")
        self.img1 = pygame.transform.scale(self.bg_img, (1200, 553))
        self.a = 1
        self.part_speed_factor = 3
        self.time = 5
        self.boss_speed_factor = 1.5
```

### game_function.py:

```python
import pygame,sys,random
from hinder import Hinder
from hinder1 import Hinder1
from bullet import  BULLET
def check_keydown_events(event,part):
    if event.key == pygame.K_RIGHT:
        part.moving_right = True
        part.direction = True
    if event.key == pygame.K_LEFT:
        part.moving_left = True
        part.direction = False
    if event.key == pygame.K_UP:
        part.isjump = True
def check_keyup_events(event,part):
    if event.key == pygame.K_RIGHT:
        part.moving_right = False
    if event.key == pygame.K_LEFT:
        part.moving_left = False
def check_events(part):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,part)
        elif event.type ==pygame.KEYUP:
            check_keyup_events(event,part)
def update_screen(game_setting,screen,part,hinders,boss,bullets,road,box,hinder1s):
    """更新屏幕上的图像"""
    #每次调用时都循环绘制屏幕
    screen.blit(game_setting.img1,(0,0))     #在游戏窗口上显示背景图片，背景图片比游戏窗口大，否则窗口周边将用黑边填充
    # screen.fill(255,0,0)
    part.blitme()
    hinders.draw(screen)
    boss.blitim()
    road.blitme()
    box.blitme()
    hinder1s.draw(screen)
    bullets.draw(screen)
    for hinder in hinders:
         part.part_hinder_collide(hinder)
    for hinder1 in hinders:
        part.part_hinder_collide(hinder1)

    # part.Ispeng()
    for bullet in bullets:
        part.part_bullet_collide(bullet)


    #绘制屏幕课件（测试）
    pygame.display.flip()
def create_fleet(game_setting, screen,hinders):
    for hinder_number in range(1):
        hinder=Hinder(game_setting, screen)
        hinder.x=0
        hinder.y =random.randint(0,500)
        hinder.rect.x=hinder.x
        hinders.add(hinder)

def create_fleet1(game_setting, screen,hinder1s):
    for hinder1_number in range(1):
        hinder1=Hinder1(game_setting, screen)
        hinder1.x=1180
        hinder1.y =random.randint(0,500)
        hinder1.rect.x=hinder1.x
        hinder1s.add(hinder1)

def create_bullet(game_setting,screen,bullets,boss):
    for bullet_number in range(10):
        bullet = BULLET(game_setting,screen)
        bullet.x = boss.rect.centerx
        bullet.y = boss.rect.bottom
        bullet.rect.x = bullet.x
        bullets.add(bullet)
```

### part.py:

```python
from time import sleep

import pygame

class Part():
    def __init__(self, game_setting, screen,box,road):
        """设置角色的初始化位置"""
        self.road=road
        self.box = box
        self.screen = screen
        self.game_setting = game_setting
        # 加载角色图像，并获得他的外解矩形位置
        self.image = pygame.image.load("image/part_0.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将新绘制的角色放在屏幕底部中间
        self.rect.centerx = self.screen_rect.centerx-200
        self.rect.centery = self.screen_rect.bottom-100
        # 在属性中储存小数值
        self.center = float(self.rect.centerx)
        self.center2 = float(self.rect.centery)
        # # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False
        self.isjump=False
        self.direction=True#角色图片的朝向
        self.ispeng=False
        self.isdie=False

    def jump(self):
        if self.game_setting.time >= -5 and not(self.isdie):
            a = self.game_setting.a  # 前半段减速上跳
            if self.game_setting.time < 0:
                a = -self.game_setting.a  # 后半段加速下落
            self.center2 -= 0.5 * a * (self.game_setting.time ** 2)  # 匀加速直线运动的位移公式
            if self.center2 < 60:
                self.center2 = 60  # 防止跳出边界
            if self.center2 > self.road.rect.top - 110:
                self.center2 = self.road.rect.top - 110  # 防止跳出边界
            self.game_setting.time -= 0.1
        else:
            a = self.game_setting.a
            self.isjump = False
            self.game_setting.time = 5
    def update(self):
        """根据移动标志调整角色的位置"""
        # 更新角色的center值，不是rect
        if not(self.isjump) and not(self.isdie) :
            if not (self.ispeng):
                if self.moving_right and self.rect.right < self.screen_rect.right:
                    self.center += self.game_setting.part_speed_factor
                if self.moving_left and self.rect.left > 0:
                    self.center -= self.game_setting.part_speed_factor
                if self.center2 != self.road.rect.top-50:
                    self.center2 = self.road.rect.top-50
            else:
                if self.moving_right and self.rect.right < self.screen_rect.right:
                    self.center += self.game_setting.part_speed_factor
                if self.moving_left and self.rect.left > 0:
                    self.center -= self.game_setting.part_speed_factor
        if not(self.isjump) and self.isdie:
            if not (self.ispeng):
                if self.center2 != self.road.rect.top:
                    self.center2 = self.road.rect.top
        if self.isjump:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center += self.game_setting.part_speed_factor
            if self.moving_left and self.rect.left > 0:
                self.center -= self.game_setting.part_speed_factor
            self.jump()

        # 根据self.center 更新 rect
        self.rect.centerx = self.center
        self.rect.centery = self.center2
        if self.isjump==True and not(self.isdie):
            self.image = pygame.image.load("image/part_1.png")
        if self.isjump==False and not(self.isdie):
            self.image = pygame.image.load("image/part_0.png")
        if self.isjump==False and self.moving_left==True and not(self.isdie):
            self.image = pygame.image.load("image/part_4.png")
        if self.isjump==False and self.moving_right==True and not(self.isdie):
            self.image = pygame.image.load("image/part_4.png")
        if self.isjump==False and self.moving_right==False and self.moving_left==False and not(self.isdie):
            self.image = pygame.image.load("image/part_0.png")
        if self.isdie:
            self.image = pygame.image.load("image/part_die.png")
    def blitme(self):
        """在指定位置绘制角色"""
        img1 = pygame.transform.flip(self.image, True, False)
        if self.direction==False:
            self.screen.blit(img1, self.rect)
        else:
            self.screen.blit(self.image, self.rect)

    def part_hinder_collide(self, hinders):
        if pygame.Rect.colliderect(pygame.Rect(self.rect.x+35, self.rect.y, 50, 80), pygame.Rect(hinders.rect.x+122, hinders.rect.y+88, 60, 60)):
            self.isdie = True

    def part_bullet_collide(self, bullets):
        if pygame.Rect.colliderect(pygame.Rect(self.rect.x+35, self.rect.y, 50, 80), pygame.Rect(bullets.rect.x, bullets.rect.y, 22, 22)):
            self.isdie = True

```

### road.py:

```python
import pygame
class Road():
    def __init__(self, game_setting, screen):
        """设置角色的初始化位置"""
        self.screen = screen
        self.game_setting = game_setting
        # 加载角色图像，并获得他的外解矩形位置
        self.image = pygame.image.load("image/road.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centery = 710
        self.img1 = pygame.transform.scale(self.image, (1200, 47))
        # 在属性中储存小数值
        self.center1 = float(self.rect.centerx)
        self.center2 = float(self.rect.centery)
    def blitme(self):
        """在指定位置绘制角色"""
        self.screen.blit(self.img1, self.rect)

```

### box.py :

```python
#箱子还没实例化出来,后续会写
import pygame
class Box():
    def __init__(self, game_setting, screen):
        """设置角色的初始化位置"""
        self.screen = screen
        self.game_setting = game_setting
        # 加载角色图像，并获得他的外解矩形位置
        self.image = pygame.image.load("image/box.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将新绘制的角色放在屏幕底部中间
        self.rect.centerx = self.screen_rect.centerx + 200
        self.rect.centery = 470
        self.img1=pygame.transform.scale(self.image,(200,40))
```

### boss.py:

```python
import pygame

#boss类
class BOSS():
    def __init__(self, screen, game_setting):
        # 初始化BOSS并设置初始位置
        self.screen = screen
        self.game_setting = game_setting
        # 加载BOSS图像
        self.image = pygame.image.load("image/boss.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 让BOSS出生在屏幕顶侧
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top
        # 在boss属性中存储小数值
        self.center = float(self.rect.centerx)
        # 移动标志
        self.moving_right = True

    def update(self):
        if self.moving_right:
            if self.center < self.screen_rect.right:
                self.center += self.game_setting.boss_speed_factor
            else:
                self.center -= self.game_setting.boss_speed_factor
                self.moving_right = False
        else:
            if self.center > self.screen_rect.left:
                self.center -= self.game_setting.boss_speed_factor
                self.moving_right = False
            else:
                self.center += self.game_setting.boss_speed_factor
                self.moving_right = True
        # # # 根据self.center跟新rect
        self.rect.centerx = self.center
    # 指定位置绘制BOSS
    def blitim(self):
        img1 = pygame.transform.flip(self.image, True, False)
        if self.moving_right==False:
            self.screen.blit(img1, self.rect)
        else:
            self.screen.blit(self.image, self.rect)
```

### bullet.py:

```python
import pygame,random
from pygame.sprite import Sprite

class BULLET(Sprite):
    def __init__(self,game_setting,screen):
        #初始化子弹位置
        super(BULLET, self).__init__()
        self.screen = screen
        self.game_setting = game_setting
        #加载子弹图像，
        self.image = pygame.image.load("image/bullet.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #让子弹出生在boss图下
        # self.rect.x = self.boss.rect.centerx
        # self.rect.y = self.boss.rect.bottom

        # 在属性中储存小数值
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 在属性中储存小数值
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # 设置子弹速度
        self.speed_factor_Y = random.randint(-5, 5)
        self.speed_factor_X = random.randint(-3,3)

    def update(self):
        self.x += self.speed_factor_X
        self.y += self.speed_factor_Y
        self.rect.y = self.y
        self.rect.x = self.x
    # def blitme(self):
    #     """在指定位置绘制角色"""
    #     self.screen.blit(self.image, self.rect)

```

### hinder.py:

```python
import pygame,random
from pygame.sprite import Sprite

class Hinder(Sprite):
    def __init__(self, game_setting, screen):
        """设置角色的初始化位置"""
        super(Hinder,self).__init__()
        self.screen = screen
        self.game_setting = game_setting
        # 加载角色图像，并获得他的外解矩形位置
        self.image = pygame.image.load("image/hinder.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将新绘制的角色放在屏幕底部中间
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 在属性中储存小数值
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #设置子弹速度
        self.speed_factor_Y = random.randint(1,2)
        self.speed_factor_X = random.randint(2,4)
    def update(self):
        self.x += self.speed_factor_X
        self.y +=self.speed_factor_Y
        self.rect.y=self.y
        self.rect.x=self.x
    # def blitme(self):
    #     """在指定位置绘制角色"""
    #     self.screen.blit(self.image, self.rect)

```

​		ps:为了省事,我直接写了个hinder1类,实际上直接用hinder在实例化一个就可以了,但是把生成位置写死了,改起来很简单,但是我有点懒:所以

### hinder1.py:

```python
import pygame,random
from pygame.sprite import Sprite

class Hinder1(Sprite):
    def __init__(self, game_setting, screen):
        """设置角色的初始化位置"""
        super(Hinder1,self).__init__()
        self.screen = screen
        self.game_setting = game_setting
        # 加载角色图像，并获得他的外解矩形位置
        self.image = pygame.image.load("image/hinder1.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将新绘制的角色放在屏幕底部中间
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 在属性中储存小数值
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #设置子弹速度
        self.speed_factor_Y = random.randint(1,2)
        self.speed_factor_X = random.randint(-4,-2)
    def update(self):
        self.x += self.speed_factor_X
        self.y +=self.speed_factor_Y
        self.rect.y=self.y
        self.rect.x=self.x
    # def blitme(self):
    #     """在指定位置绘制角色"""
    #     self.screen.blit(self.image, self.rect)

```

​	

​		代码完成的很草率,有很多地方还能优化,死亡画面和计分都没加

后续完成:	功能(boss血量,主人公血量,死亡画面,等)

​					函数(代码整合优化,主人公攻击boss,计分,等)

```python
#代码完成:
@by本人
	main_cycle,game_function,part,settings,部分整合
@by Siranyu
	boss,bullet,部分整合	
@by 小zhang
	hinder,hinder1,road,box
```

​	