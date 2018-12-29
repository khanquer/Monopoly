from classes import *
import pygame, sys, random
from players import *
from init import *
from draw import *
#from classes import Prop

RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)



def main():
#	print ("Hello World")
#       init.main()
        file = open("src.txt","r")
	(tileList,playerList) = initVars()

	for Tile1 in tileList:
		print(Tile1)


        for P1 in playerList:
		print(P1)
	
	pygame.init()
	screen = pygame.display.set_mode((1540,1040))
	clock = pygame.time.Clock()
	Loop = True
		
	TURN = 0

	sRoll = True
	sBuy = False
	sAuction = False
	sTrade = False
	sBuild = False
	sEnd = False
	
	drawCanvas(screen,tileList)
	drawPlayers(screen,playerList)
	drawButtons(screen,sRoll,sBuy,sAuction,sTrade,sBuild,sEnd)
	drawPanel(screen,TURN,playerList,tileList)


	
	while Loop:
#		print('Loop')
		for event in pygame.event.get():
#			print(event)
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_r):
				if sRoll == True:
					sRoll = False
					print("Action = Roll")
					pos = roll(screen,TURN,playerList)
					print(tileList[playerList[TURN].loc])
					print(type(tileList[playerList[TURN].loc]) is Prop)
					print(isinstance(tileList[playerList[TURN].loc],Prop))
#					If Unowned, buy, else, end 
					if isinstance(tileList[playerList[TURN].loc],Prop) == True:	
						if tileList[pos].owner == -1:
							sBuy = True
							sEnd = False
						else:
							sEnd = True
							sBuy = False
					else:
						sEnd = True
						sBuy = False

					update(screen,TURN,tileList,playerList,sRoll,sBuy,sAuction,sTrade,sBuild,sEnd)
			if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
				if sBuy == True:
					sRoll = False
					sBuy = False
					sEnd = True
					print("Action = Buy")
					buy(screen,TURN,playerList,tileList)
					update(screen,TURN,tileList,playerList,sRoll,sBuy,sAuction,sTrade,sBuild,sEnd)
			if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
				if sEnd == True:
					sRoll = True
					sEnd = False
					sBuy = False
					print("Action = End")
					TURN += 1
					TURN %= 4
#					num = roll(screen,TURN,playerList)
					update(screen,TURN,tileList,playerList,sRoll,sBuy,sAuction,sTrade,sBuild,sEnd)
			
			
		pygame.display.update()
		clock.tick(10)


def update(screen,TURN,tileList,playerList,sRoll,sBuy,sAuction,sTrade,sBuild,sEnd):
	
	drawCanvas(screen,tileList)
	drawPlayers(screen,playerList)
	drawButtons(screen,sRoll,sBuy,sAuction,sTrade,sBuild,sEnd)
	drawPanel(screen,TURN,playerList,tileList)

def buy(screen,TURN,playerList,tileList):
	playerList[TURN].propList.append(playerList[TURN].loc)
	playerList[TURN].propList.sort()
	tileList[playerList[TURN].loc].owner = TURN
	
	playerList[TURN].money -= tileList[playerList[TURN].loc].cost

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
	return playerList[TURN].loc




if __name__ == "__main__":
#	print("RUN AS MAIN")
	main()
