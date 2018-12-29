from classes import *
import pygame, sys
from players import *





def main():
    v = initVars()



def initVars():
    file = open("src.txt","r")
    tileList = []
    i = 0
    for line in file:
        line = line.strip()
        if(i == 0):
            i += 1
            continue
        setTiles(line,tileList)
        i+=1

    playerList = []
    setPlayers(playerList)
    return tileList,playerList

def setPlayers(playerList):
	for i in range(0,4):
		m = []
		x = Players(i,0,m)
		playerList.append(x)
	

def setTiles(line,tileList):
	m = line.split()
	print(m)
	
	tileID = int(m[0])	
#	print("TileID = " + str(tileID) + ' | ')
	name = m[1]
#	print("Name = " + name +  ' | ')

	if (m[2] == 'True'):
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
		x = Tile(tileID,name)
		tileList.append(x)
#		print("isProp = False " +  ' | ')

if __name__ == "__main__":
    main()
    
