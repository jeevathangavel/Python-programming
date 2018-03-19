a,b,c=raw_input().split()
a=int(a)
b=int(b)
c=int(c)
if((a>b) and (a>c)):
	print("a is large")
elif((b>a)and (b>c) ):
	print("b is large")
else:
	print("c is large")
