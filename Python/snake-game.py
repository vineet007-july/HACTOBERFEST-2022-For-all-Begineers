import pygame
import random
import sys

def Snake_pos_reset_x():
	if 0 < Snake_pos[0] < Width - Snake_size:
		pass
	elif Snake_pos[0] < 0:
		Snake_pos[0] = Width - Snake_size
	else:
		Snake_pos[0] = 0

def Snake_pos_reset_y():
	if 0 < Snake_pos[1] < Height - Snake_size:
		pass
	elif Snake_pos[1] < 0:
		Snake_pos[1] = Height - Snake_size
	else:
		Snake_pos[1] = 0

def detect_collision():
	p_x = Snake_pos[0]
	p_y = Snake_pos[1]

	f_x = food_pos[0]
	f_y = food_pos[1]

	if (f_x >= p_x and f_x < (p_x + Snake_size)) or (p_x >= f_x and p_x < (f_x+food_size)):
		if (f_y >= p_y and f_y < (p_y + Snake_size)) or (p_y >= f_y and p_y < (f_y+food_size)):
			return True
	return False

def detect_collision_life():
	p_x = Snake_pos[0]
	p_y = Snake_pos[1]

	f_x = life_pos[0]-(life_size//2)
	f_y = life_pos[1]-(life_size//2)

	if (f_x >= p_x and f_x < (p_x + Snake_size)) or (p_x >= f_x and p_x < (f_x+life_size)):
		if (f_y >= p_y and f_y < (p_y + Snake_size)) or (p_y >= f_y and p_y < (f_y+life_size)):
			return True
	return False

def detect_collision_snake():
	Snake_pos = record[len(record)-1]
	for i in range(len(record)-2):
		if record[i] == Snake_pos:
			return True
	return False
		
def print_snake(Colour):
	for i in record:
		pygame.draw.rect(screen, Colour, (i[0], i[1], Snake_size, Snake_size))

pygame.init()

Width = 800 # x
Height= 700 # y
Red = (255, 0, 0)
Blue = (30, 0, 255)
Light_Blue = (9, 219, 220)
Green = (0, 255, 0)
Lime_Green = (50,205,50)
Orange = (252, 78, 7)
Black = (0, 0, 0)
White = (255, 255, 255)
Snake_size = 50
food_size = 40
life_size = 20
Snake_pos = [Width/2, Height/2]
Snake_pos_change_x, Snake_pos_change_y, score, life = 0, 0, 0, 0
Snake_length = 1
changed = 3
life_on = 20
speed = 100
food_pos = [random.randrange(0, Width - food_size), random.randrange(0, Height - food_size)]
life_pos = [random.randrange(0 + (life_size//2), Width - (life_size//2)), random.randrange(0 + (life_size//2), Height - (life_size//2))]
myFont = pygame.font.SysFont("monospace", 35)
myFont1 = pygame.font.SysFont("chiller", 35)
record = []
in_x_axis = True
in_y_axis = True
fps = pygame.time.Clock()

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('SnAKe_gAMe')

running = True

while running:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:

			if in_y_axis:
				if event.key == pygame.K_LEFT:
					Snake_pos_change_x = -changed
					Snake_pos_change_y = 0
					in_x_axis = True
					in_y_axis = False
				if event.key == pygame.K_RIGHT:
					Snake_pos_change_x = changed
					Snake_pos_change_y = 0
					in_x_axis = True
					in_y_axis = False
				
				
			if in_x_axis:
				if event.key == pygame.K_UP:
					Snake_pos_change_y = -changed
					Snake_pos_change_x = 0
					in_y_axis = True
					in_x_axis = False
				if event.key == pygame.K_DOWN:
					Snake_pos_change_y = changed
					Snake_pos_change_x = 0
					in_y_axis = True
					in_x_axis = False

			if event.key == pygame.K_SPACE:
				speed = 300

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:      
				speed = 100			
				

	Snake_pos[0] += Snake_pos_change_x
	Snake_pos[1] += Snake_pos_change_y

	screen.fill(Light_Blue)
	pygame.draw.rect(screen, Lime_Green,(food_pos[0], food_pos[1], food_size, food_size))
	if score%life_on == 0 :
		pygame.draw.circle(screen, Green, (life_pos[0], life_pos[1]), life_size//2)

	Snake_pos_reset_x()
	Snake_pos_reset_y()

	collision = detect_collision()
	collision_life = detect_collision_life()

	if collision :
		food_pos.clear()
		food_pos = [random.randrange(0, Width - food_size), random.randrange(0, Height - food_size)]
		score += 1
		Snake_length += 10

	if collision_life:
		if score%life_on == 0:
			score += 1
			life += 1
			life_pos.clear()
			life_pos = [random.randrange(0, Width - life_size), random.randrange(0, Height - life_size)]


	if score > 0 :
		snake_collision = detect_collision_snake()
		if snake_collision :
			running = False

	new_pos = []
	new_pos.append(Snake_pos[0])
	new_pos.append(Snake_pos[1])
	record.append(new_pos)

	if len(record) > Snake_length :
		del record[0]

	print_snake(Red)

	text = "Score:" + str(score)
	label = myFont.render(text, 1, Black)
	screen.blit(label, (Width - 180, Height-680))

	text = "Life :" + str(life)
	label = myFont.render(text, 1, Black)
	screen.blit(label, (Width - 180, Height-650))

	text = "Press SPACE to speed up..."
	label = myFont.render(text, 1, Black)
	screen.blit(label, (Width - 780, Height-680))
			
	while running == False:
		if life > 0:
			life -= 1
			running = True
			break
		screen.fill(Light_Blue)
		label = myFont1.render("Press R to Play Again or Q to Quit", True, Black)
		screen.blit(label, (Width//2-200, Height//2-50))

		text = "Score:" + str(score)
		label = myFont1.render(text, 1, Black)
		screen.blit(label, (Width//2-50, Height-350))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					running = True
					Snake_pos = [Width/2, Height/2]
					record.clear()
					score = 0
					Snake_length = 1
					Snake_pos_change_x = 0
					Snake_pos_change_y = 0

				if event.key == pygame.K_q:
					sys.exit()

		pygame.display.update()

	fps.tick(speed)
	pygame.display.update()
	
