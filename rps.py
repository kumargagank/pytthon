import random
l=["r","p","s"]
us=0
cs=0
d = {'r':'rock','p':'paper','s':'scissor'}
while True:
	#take input from user
	
	u=input("enter your choice, press n to discontinue")
	if u in d:
		print(u,d[u])
	#to exit
	if u == 'n':
		print("Game over")
		print("user score",us)
		print("comp score",cs)
		if us==cs:
			print("tie")
		elif us>cs:
			print("user wins")
		else :
			print("comp wins")
		exit()
	#input from computer
	c = random.choice(l)
	print("computer chooses", c)
	if c in d:
		print(c,d[c])

	#compare the user and computer choice
	if u == c:
		print("tie")
	elif u=="r" and c=="p":
		print("comp wins")
		cs=cs+1
	elif u=="r" and c=="s":
		print("user wins")
		us=us+1
	elif u=="p"	and c=="s":
		print("comp wins")
		cs=cs+1
	elif u=="p" and c=="r":
		print("user wins")
		us=us+1
	elif u=="s"	and c=="r":
		print("comp wins")
		cs=cs+1
	elif u=="s"	and c=="p":
		print("user wins")
	else:
		print("invalid")	


