import pygame
import random

#iniciar pygame
pygame.init()

'''
todo lo que pase dentro de una pantalla de pygame es un evento TODO y podemos usar eso a nuestro favor
'''

#create screen
screen = pygame.display.set_mode((800, 600))

#create background
background = pygame.image.load('background.jpg')

#change title
pygame.display.set_caption('Space Invaiders')

#change icon
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)

# create character (64 pixels)
character_img = pygame.image.load('space-ship.png')

# initial potition
character_x = 368
character_y = 510

# variables for adding movement
character_x_change = 0
character_y_change = 0

# create enemy (32 pixeles)
enemy_img = pygame.image.load('enemy.png')

# initial potition of enemy
enemy_x = random.randint(32,768)
enemy_y = random.randint(0, 300)

# variables for adding movement for enemy
enemy_x_change = 0.2
enemy_y_change = 25

# create bullet (16 pixeles)
bullet_img = pygame.image.load('balas.png')

# initial potition of bullet
bullet_x = 0
bullet_y = 510

# variables for adding movement for bullet
bullet_x_change = 0
bullet_y_change = 0.5

#create a varible to shot the bullet
bullet_shot = False

#create explotion
explotion_img = pygame.image.load('explode.png')

#position of explotion
explotion_x = 0
explotion_y = 0

#Creating score
score = 0

'''
tener en cuenta los pixeles que miden los objetos y la pantalla al momento de introducir la locacion inicial
hacer las sumas o restas necesarias para tener coordenadas exactas 
'''

#contruction of character and coordenates initials
def character( x, y):
	screen.blit(character_img, (x, y))

#contruction of enemy and coordenates initials
def enemy( x, y):
	screen.blit(enemy_img, (x, y))

#contruction of the bullet
def shot_bullet( x, y):
	global bullet_shot
	bullet_shot = True
	screen.blit(bullet_img, (x + 24,y))

#create colision
def colision( x_2, x_1, y_2, y_1):
	contact = (((x_2 - x_1)**2)+((y_2 - y_1)**2))**(1/2)
	if contact < 27:
		return True
	else:
		return False

#create explotion (64 pixels)
def explotion( x , y):
	screen.blit(explotion_img, (x,y))

#loop of the game
ejecucion = True
while ejecucion:
	#add background
	screen.blit(background, (0,0))

	#get events
	for evento in pygame.event.get():

		# quit button
		if evento.type == pygame.QUIT:
			ejecucion = False

		# movement of character and get it by events
		if evento.type == pygame.KEYDOWN:
			if evento.key == pygame.K_LEFT:
				character_x_change -= 0.4
			if evento.key == pygame.K_RIGHT:
				character_x_change += 0.4
			if evento.key == pygame.K_SPACE:
				if not bullet_shot:
					bullet_x = character_x
					shot_bullet(bullet_x, character_y)

		# stop movingof character and get it by event
		if evento.type == pygame.KEYUP:
			if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
				character_x_change = 0

	# add the movement to the character with the keys
	character_x += character_x_change

	# limits of movement of character
	if character_x > 734:
		character_x = 734
	elif character_x < 0:
		character_x = 0

	# add the movement to the enemy with the keys
	enemy_x += enemy_x_change

	# limits of movement of enemy in x
	if enemy_x > 740:
		enemy_x_change = -0.2
		enemy_y += enemy_y_change
	elif enemy_x < 60:
		enemy_x_change = 0.2
		enemy_y += enemy_y_change

	# limit of bullet and reboot
	if bullet_y < 0:
		bullet_y = 510
		bullet_shot = False

	# adding movement to bullet
	if bullet_shot:
		shot_bullet(bullet_x, bullet_y)
		bullet_y -= bullet_y_change

	#adding colision
	destroy = colision(bullet_x, enemy_x, bullet_y, enemy_y)
	if destroy:
		bullet_y = 510
		bullet_shot = False
		score += 10
		enemy_x = random.randint(32, 768)
		enemy_y = random.randint(0, 300)


	# create character and move character
	character(character_x, character_y)

	# create and move enemy
	enemy(enemy_x, enemy_y)

	#refresh the screen
	pygame.display.update()

