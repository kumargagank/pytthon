class Test:
	h = 0

	def __init__(self):
		self.h = 6

	def my__func(self,k):
		print("i am in the class")
		self.h = k #assigning the value
		print(self.h)

o=Test()			
print(o.h)
o1=Test()
print(o1.h)
o.my__func(4)
o1.my__func(6)
o3=Test()
print(o3.h)