class Tile(object):
	def __init__(self,tileID,name):
		self.tileID = tileID
		self.name = name
	def __str__(self):
		return ( "TileID = " + str(self.tileID) + " | Name = "  + self.name )

class Prop(Tile):
	def __init__(self,tileID,name,cost,owner):
		super(Prop,self).__init__(tileID,name)
		self.cost = cost
		self.owner = owner

	def __str__(self):
		return super(Prop,self).__str__() + " | Cost = " + str(self.cost) + " | Owner = " + str(self.owner)

class CProp(Prop):
	def __init__(self,tileID,name,cost,owner,color):
		super(CProp,self).__init__(tileID,name,cost,owner)
		self.color = color

	def __str__(self):
		return super(CProp,self).__str__() + " | Color = " + self.color

class RProp(Prop):
	def __init__(self,tileID,name,cost,owner,num):
		super(RProp,self).__init__(tileID,name,cost,owner)
		self.num = num

	def __str__(self):
		return super(RProp,self).__str__() + " | Num = " + self.num

class UProp(Prop):
	def __init__(self,tileID,name,cost,owner,num):
		super(UProp,self).__init__(tileID,name,cost,owner)
		self.num = num

	def __str__(self):
		return super(UProp,self).__str__() + " | Num = " + self.num

