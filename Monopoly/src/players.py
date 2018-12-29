class Players(object):
	def __init__(self,num,loc,pL):
		self.num = num
		self.loc = loc
		self.propList = pL
		self.money = 1500
	def __str__(self):
		#return ( "num = " + str(self.num) + " | loc = "  + str(self.loc)+ " | propList = " + str(self.propList))
		return ( str(self.num) + " | loc = "  + str(self.loc)+ " | $ = " + str(self.money) + " | propList = " + str(self.propList))

