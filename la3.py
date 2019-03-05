a = 10
b = 14
c = 12

if(a >= b) and (b >= c):
	largest = a

elif(b >= a) and (b >= c):
	largest = b

else:
	largest = c

print("the largest number between",a,",",b,"and",c,"is",largest)		     	