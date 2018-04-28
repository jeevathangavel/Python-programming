a,b,c=raw_input().split()
a=int(a)
b=int(b)
c=int(c)
s=0
for i in range(1,a+1):
	z=b+(i-1)*c
	s=s+z
print s,
