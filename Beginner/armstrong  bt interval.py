a,b=raw_input().split()
a=int(a)
b=int(b)
l=[]
s=0
for i in range(a+1,b):
	x=str(i)
	p=len(x)
	for j in range(0,p):
		l.append(x[j])
	for k in range(0,p):
		s=s+(int(l[k])**3)
	l=[]
	if(s==int(x)):
		print s,
		s=0
	else:
		s=0
	
