a=raw_input()
b=len(a)
l=[]
s=0
for i in range(0,b):
	l.append(int(a[i]))
for i in range(0,b):
	s=s+(l[i]**3)
if(s==int(a)):
	print "yes"
else:
	print"no"

	
	
