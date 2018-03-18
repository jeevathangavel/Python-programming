a=raw_input()
if a.isdigit():
	a=int(a)
	if(a<0):
		print "neg"
	elif(a==0):
		print "zero"
	else:
		print "pos"
