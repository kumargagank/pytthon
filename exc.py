l=[1,2,3,4,5,6]
try:
	s=len(l)
	if s>4:
		raise TypeError
	print(d[l])


except TypeError:
	print("error!!!! length should be less")
except NameError:
	print("Index out of range")
else:
	for i in l:
		print(l)
finally:
	print("Execution done!!!!")