from classes import *
import pygame, sys
from players import *
import random
#from classes import Prop

RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

def main():
	#print ("Hello World")
	file = open("src.txt","r")
	tileList = []

	i = 0
	for line in file:
		line = line.strip()
		if(i == 0):
			i+=1
			continue
#		print(line)
		
		setTiles(line,tileList)
		i+=1

	for Tile1 in tileList:
		print(Tile1)

	playerList = []
	setPlayers(playerList)

	for P1 in playerList:
		print(P1)
	
	pygame.init()
	screen = pygame.display.set_mode((1040,1040))
	clock = pygame.time.Clock()
	Loop = True
	TURN = 0
	
	sRoll = True
	sBuy = True
	sEnd = True
	
	drawCanvas(screen,tileList)
	drawPlayers(screen,playerList)
	drawButtons(screen,sRoll,sBuy,sEnd)
	
	while Loop:
#		print('Loop')
		for event in pygame.event.get():
#			print(event)
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				drawCanvas(screen,tileList)
				roll(screen,TURN,playerList)
				TURN += 1
				TURN = TURN%4
				drawPlayers(screen,playerList)
				drawButtons(screen,sRoll,sBuy,sEnd)
			
		pygame.display.update()
		clock.tick(10)
			

'''
			pressed = pygame.key.get_pressed()
			if pressed[pygame.K_UP]: dir1 = 'up'
			if pressed[pygame.K_DOWN]: dir1 = 'down'
			if pressed[pygame.K_LEFT]: dir1 = 'left'
			if pressed[pygame.K_RIGHT]: dir1 = 'right'
			
		if dir1 == 'up': y -= 30
		if dir1 == 'down': y += 30
		if dir1 == 'left': x -=30
		if dir1 == 'right': x +=30
		screen.fill((0,0,0))
		
		if is_Blue: color = (0,128,255)
		else:color = (255,100,0)		
		pygame.draw.rect(screen,color,pygame.Rect(x,y,30,30))
'''
#		drawCanvas(screen)

	
#	print(tileList[0])


def roll(screen,TURN, playerList):
#GEN TO 2 RANDOM NUMBERS FOR THE DICE
	num1 = random.randint(1,6)
	num2 = random.randint(1,6)
	num = num1 + num2
#	num = 5
	playerList[TURN].loc += num
	playerList[TURN].loc = playerList[TURN].loc%40
	sys_font = pygame.font.SysFont("None",30)
	text1 = sys_font.render(str(num1),0,(0,0,0))
	text2 = sys_font.render(str(num2),0,(0,0,0))
	text = sys_font.render(str(num),0,(0,0,0))
	screen.blit(text1,(250,300))
	screen.blit(text2,(290,300))
	screen.blit(text,(270,320))

def drawButtons(screen,sRoll,sBuy,sEnd):	
	color = RED
	pygame.draw.rect(screen,color,pygame.Rect(260,500,120,60))
	color = GREEN
	pygame.draw.rect(screen,color,pygame.Rect(460,500,120,60))	
	color = BLUE
	pygame.draw.rect(screen,color,pygame.Rect(660,500,120,60))
	color = WHITE
	sys_font = pygame.font.SysFont("None",25)
	text1 = sys_font.render('ROLL',0,WHITE)	
	text2 = sys_font.render('BUY',0,WHITE)
	text3 = sys_font.render('END',0,WHITE)
	screen.blit(text1,(290,520))	
	screen.blit(text2,(490,520))
	screen.blit(text3,(690,520))

	
def drawPlayers(screen,playerList):
	for i in range(0,4):
		
		diffx = 0
		diffy = 0
		if (i == 0): 
			color = (255,140,0)
			diffx = 0
			diffy = 0
		if (i == 1): 
			color = (255,0,0)
			diffx = 20
			diffy = 0
		if (i == 2): 
			color = (0,255,0)
			diffx = 0
			diffy = 20
		if (i == 3): 
			color = (0,0,255)
			diffx = 20
			diffy = 20

		ID = playerList[i].loc
		#BOTTOM ROW
		if ((ID/10) < 1 ):
			pygame.draw.circle(screen,color,(900-ID*80 + diffx,960 + diffy),10)
		#LEFT ROW
		elif ((ID/10) < 2 ):
			num = ID%10
			pygame.draw.circle(screen,color,(40 + diffx,910-num*80+diffy),10)
#			pygame.draw.rect(screen,color,pygame.Rect(122,882-num*80,38,78))
		#TOP ROW
		elif ((ID/10) < 3 ):
			num = ID%10
			pygame.draw.circle(screen,color,(100 + num*80 + diffx,40 + diffy),10)
		#RIGHT ROW
		elif ((ID/10) < 4 ):
			num = ID%10
			pygame.draw.circle(screen,color,(980 + diffx,100 + num*80 + diffy),10)
#			pygame.draw.rect(screen,color,pygame.Rect(882,82+num*80,38,78))



	
def drawCanvas(screen,tileList):
	screen.fill((66,244,238))
	color = (0,0,0)
	pygame.draw.rect(screen,color,pygame.Rect(0,880,1040,3))
	pygame.draw.rect(screen,color,pygame.Rect(160,0,3,1040))
	pygame.draw.rect(screen,color,pygame.Rect(0,160,1040,3))
	pygame.draw.rect(screen,color,pygame.Rect(880,0,3,1040))
	
	pygame.draw.rect(screen,color,pygame.Rect(160,920,720,2))	
	pygame.draw.rect(screen,color,pygame.Rect(120,160,2,720))
	pygame.draw.rect(screen,color,pygame.Rect(160,120,720,2))
	pygame.draw.rect(screen,color,pygame.Rect(920,160,2,720))
	
#Drawing the boundary Lines
	for i in range(1,9):
		pygame.draw.rect(screen,color,pygame.Rect(160+80*i,880,2,160))
		pygame.draw.rect(screen,color,pygame.Rect(0,160+80*i,160,2))	
		pygame.draw.rect(screen,color,pygame.Rect(160+80*i,0,2,160))
		pygame.draw.rect(screen,color,pygame.Rect(880,160+80*i,160,2))

#Tile Loop
	for tile1 in tileList:
		ID = tile1.tileID

#Drawing rectangles for the color props
		if (type(tile1) is CProp):
#			print(str(ID) + " IS CPROP " + tile1.color)
			if (tile1.color == 'Purple'): color = (72,61,139)	
			if (tile1.color == 'Blue'): color = (0,191,255)
			if (tile1.color == 'Pink'): color = (218,112,214)
			if (tile1.color == 'Orange'): color = (255,140,0)
			if (tile1.color == 'Red'): color = (255,0,0)
			if (tile1.color == 'Yellow'): color = (255,255,0)
			if (tile1.color == 'Green'): color = (34,139,34)
			if (tile1.color == 'DBlue'): color = (0,0,205)
			
			#BOTTOM ROW
			if ((ID/10) < 1 ):
				pygame.draw.rect(screen,color,pygame.Rect(882-ID*80,882,78,38))
			#LEFT ROW
			elif ((ID/10) < 2 ):
				num = ID%10
				pygame.draw.rect(screen,color,pygame.Rect(122,882-num*80,38,78))
			#TOP ROW
			elif ((ID/10) < 3 ):
				num = ID%10
				pygame.draw.rect(screen,color,pygame.Rect(82+num*80,122,78,38))
			#RIGHT ROW
			elif ((ID/10) < 4 ):
				num = ID%10
				pygame.draw.rect(screen,color,pygame.Rect(882,82+num*80,38,78))

#WRITING THE TEXT
		sys_font = pygame.font.SysFont("None",15)
		text = sys_font.render(tile1.name,0,(0,0,0))

		#BOTTOM ROW
		if ((ID/10) < 1 ):
			num = ID%10
			locx = 885 - num*80
			locy = 940		
		#LEFT ROW
		elif ((ID/10) < 2 ):
			num = ID%10
			locx = 90
			locy = 890 - num*80
			text = pygame.transform.rotate(text,270)
		#TOP ROW	
		elif ((ID/10) < 3 ):
			num = ID%10
			locx = 80 + 80*num
			locy = 90
			text = pygame.transform.rotate(text,180)
		#RIGHT ROW
		elif ((ID/10) < 4 ):
			num = ID%10
			locx = 940
			locy = 100 + 80*num
			text = pygame.transform.rotate(text,90)
		screen.blit(text,(locx,locy))



def setPlayers(playerList):
	for i in range(0,4):
		m = []
		x = Players(i,0,m)
		playerList.append(x)
	

def setTiles(line,tileList):
	m = line.split()
#	print(m)
	
	tileID = int(m[0])	
#	print("TileID = " + str(tileID) + ' | ')
	name = m[1]
#	print("Name = " + name +  ' | ')

	if (m[2] == 'True'):
		b = True
#		print("isProp = True " +  ' | ')
		cost = int(m[5])
#		print ("cost = " + m[4])

		if(m[3] == 'Col'):
			color = m[4]
			x = CProp(tileID,name,cost,-1,color)
			tileList.append(x)
		elif(m[3] == 'Rail'):
			num = m[4]
			x = RProp(tileID,name,cost,-1,num)
			tileList.append(x)
		else:
			num = m[4]
			x = UProp(tileID,name,cost,-1,num)
			tileList.append(x)

#		x = Prop(tileID,name,cost)
#		tileList.append(x)
	else:
		b = False
#		print("isProp = False " +  ' | ')
		x = Tile(tileID,name)
		tileList.append(x)
	
	
#	x = Tile(i,name)
#	tileList.append(x)

#	print("isProp = " + str(b))


if __name__ == "__main__":
#	print("RUN AS MAIN")
	main()

