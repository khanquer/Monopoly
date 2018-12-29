from classes import *
import pygame, sys
from players import *

RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (211,211,211)
TURQ = (66,244,197)

def drawPanel(screen,TURN,playerList,tileList):
	pygame.draw.rect(screen,BLACK,pygame.Rect(1040,0,10,1040))
	pygame.draw.rect(screen,TURQ,pygame.Rect(1050,0,490,1040))
	sys_font = pygame.font.SysFont("None",25)
	tp0 = str(playerList[0])
	textP0 = sys_font.render(tp0,0,BLACK)
	tp1 = str(playerList[1])
	textP1 = sys_font.render(tp1,0,BLACK)
	tp2 = str(playerList[2])
	textP2 = sys_font.render(tp2,0,BLACK)
	tp3 = str(playerList[3])
	textP3 = sys_font.render(tp3,0,BLACK)

	screen.blit(textP0,(1060,750))
	screen.blit(textP1,(1060,800))
	screen.blit(textP2,(1060,850))
	screen.blit(textP3,(1060,900))

def drawButtons(screen,sRoll,sBuy,sAuction,sTrade,sBuild,sEnd):
	color = RED
	if (sRoll == False):
		color = GRAY
	pygame.draw.rect(screen,color,pygame.Rect(260,500,120,60))
	color = GREEN
	if (sBuy == False):
		color = GRAY
	pygame.draw.rect(screen,color,pygame.Rect(460,500,120,60))	
	color = BLUE
	if (sAuction == False):
		color = GRAY
	pygame.draw.rect(screen,color,pygame.Rect(660,500,120,60))
	color = RED
	if (sTrade == False):
		color = GRAY
	pygame.draw.rect(screen,color,pygame.Rect(260,600,120,60))
	color = GREEN
	if (sBuild == False):
		color = GRAY
	pygame.draw.rect(screen,color,pygame.Rect(460,600,120,60))	
	color = BLUE
	if (sEnd == False):
		color = GRAY
	pygame.draw.rect(screen,color,pygame.Rect(660,600,120,60))
	color = WHITE
	sys_font = pygame.font.SysFont("None",25)
	text1 = sys_font.render('ROLL',0,WHITE)	
	text2 = sys_font.render('BUY',0,WHITE)
	text3 = sys_font.render('AUCTION',0,WHITE)
	text4 = sys_font.render('TRADE',0,WHITE)
	text5 = sys_font.render('BUILD',0,WHITE)
	text6 = sys_font.render('END',0,WHITE)
	screen.blit(text1,(290,520))
	screen.blit(text2,(490,520))
	screen.blit(text3,(690,520))
	screen.blit(text4,(290,620))
	screen.blit(text5,(490,620))
	screen.blit(text6,(690,620))
	
	
def drawPlayers(screen,playerList):
	for i in range(0,4):
		#Player positions wrt the first
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
                        text  = pygame.transform.rotate(text,180)
                #RIGHT ROW
		elif ((ID/10) < 4 ):
			num = ID%10
			locx = 940
			locy = 100 + 80*num
			text = pygame.transform.rotate(text,90)
		screen.blit(text,(locx,locy))



