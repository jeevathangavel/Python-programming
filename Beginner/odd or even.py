a=raw_input()
if a.isdigit():
	a=int(a)
	if(a%2==0):
		print("a is even")
	else:
		print("a is odd")
else:
	print("invalid")
