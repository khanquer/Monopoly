class Players(object):
	def __init__(self,num,loc,pL):
		self.num = num
		self.loc = loc
		self.propList = pL
	def __str__(self):
		return ( "num = " + str(self.num) + " | loc = "  + str(self.loc)+ " | propList = " + str(self.propList))

