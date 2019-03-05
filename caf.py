#creating a function

def func1():
	print("hiiiii")

func1()

#with 2 parameter
def func2(a,b):
	c=a+b
	print(c)

func2(2,3)


def func3(a):
	print("hi"+a)
	
func3("GAGAN")	


#default parameter
def func4(university = "ITB"):
	print("I am in" +"\t"+ university)
func4("ITD")
func4("IOT")
func4()

#calling one function to other 
def func5():
	print("hi")
def func6():
	print("hello")
	func5()
	func6()

#with parameter
def func5(a,b):
	print("hii")
	c=a+b
	print(C)

def func6():
	print("hii")
	func5(2,3)	
	func6()

#return function
def func5(a,b):
	print("hii")
	c=a+b
	return c
def func6():
	print("HELLO")
	S=func5(2,7)
	print("aadition is",S)
	func6()
