import pygame
import sys
from random import randint

pygame.font.init()

FPS = 50
W = 1000
H = 700

x_gun = W/2-40
x_bullet = x_gun+40
y_bullet = 570 
r_bullet = 5
dy_bullet = 3 #bullet speed
dx_set = 3 #скорость пухи
y_gun = 575
y_sh1 = H/2-50
y_sh2 = H/2-140
y_sh3 = H/2-250
x_sh1 = randint(0, W-100)
x_sh2 = randint(0, W-60)
x_sh3 = randint(0, W-40)
dx_sh1, dx_sh2, dx_sh3 = (1, -2, 3) #скорости кораблей
color1 = 'white'
shoot = 0

sc = pygame.display.set_mode((W,H))
sea_sc = pygame.Surface((W,H/2))
road_sc = pygame.Surface((W,H/5.5))
clock = pygame.time.Clock()



while 1:
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			sys.exit()

	x_sh1+=dx_sh1
	if x_sh1>W-100 or x_sh1<0:
		dx_sh1 = -dx_sh1

	x_sh2+=dx_sh2
	if x_sh2>W-60 or x_sh2<0:
		dx_sh2 = -dx_sh2

	x_sh3+=dx_sh3
	if x_sh3>W-40 or x_sh3<0:
		dx_sh3 = -dx_sh3

	keys = pygame.key.get_pressed() # управление пухой
	if keys[pygame.K_RIGHT] and x_gun<W-45:
		x_gun+=dx_set
	elif keys[pygame.K_LEFT]and x_gun>-35:
		x_gun-=dx_set
							
	if keys[pygame.K_UP]:
		shoot = 1 # пуля летит
	if shoot == 1:	
		y_bullet -= dy_bullet			
		if y_bullet <= 0:
			shoot = 0
			y_bullet = 570
			x_bullet = x_gun + 40
		elif y_bullet == y_sh1+6 and x_sh1<=x_bullet<=x_sh1+100:
			pygame.time.delay(1000)
			shoot = 0
			y_bullet = 570
			x_bullet = x_gun + 40

	elif shoot == 0:
		x_bullet = x_gun + 40


	sc.fill('#F4A460')
	sea_sc.fill('#00FFFF')
	sc.blit(sea_sc, (0,30))
	road_sc.fill('black')
	sc.blit(road_sc, (0, 550))
	pygame.draw.circle(sc, '#C71585', (x_bullet,y_bullet), r_bullet)
	pygame.draw.rect(sc, color1, (x_sh1, y_sh1, 100, 20))
	pygame.draw.rect(sc, color1, (x_sh2, y_sh2, 60, 20)) # сделать ооп
	pygame.draw.rect(sc, color1, (x_sh3, y_sh3, 40, 20))
	pygame.draw.rect(sc, 'white', (x_gun, y_gun, 80, 30))

	pygame.display.update()
	clock.tick(FPS)
