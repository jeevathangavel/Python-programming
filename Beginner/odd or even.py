a=raw_input()
if a.isdigit():
	a=int(a)
	if(a%2==0):
		print("even")
	else:
		print("odd")
else:
	print("invalid")
