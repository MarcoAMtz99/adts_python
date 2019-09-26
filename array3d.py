class array3d:
	def __init__(self,rows,cols,depth):
		self.__rows=rows
		self.__cols=cols
		self.__depth=depth
		self.__data=[]
		for i in range(self.__depth):
			aux=[]
			for j in range (self.__rows):
				aux2=[]
				for c in range (self.__cols):
					aux2.append(None)
					aux.append(aux2)
			self.__data.append(aux)
	def to_String(self):
		print(self.__data)
	def get_num_depth(self):
		return self.__depth
	def get_num_rows(self):
		return self.__rows
	def get_num_cols(self):
		return self.__cols
	def set_item(self,rows,cols,depth,value):
		self.__data[depth][rows][cols]=value
	def get_item(self,rows,cols,depth):
		return self.__data[depth][rows][cols]
	
    def clearing (self,value):
		for i in range (self.__depth):
			for j in range (self.__rows):
				for x in range (self.__cols):
					self.set_item(j,x,i,value)


'''
def main():
	a3d=array3d(34,34,12)
    
	a3d.to_String()
	a3d.clearing(5)
	a3d.to_String()
main()
'''
