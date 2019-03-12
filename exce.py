#Exception
try:	
	d=[7,6,8,9]
	print(d)
	print(d[5])
	if d > 9:
		raise TypeError
	elif d > 3:
	 	raise IndexError
except IndexError:
	print("index error")

except TypeError:
	print("type error")		
	
finally:	
	print("Execution completed")