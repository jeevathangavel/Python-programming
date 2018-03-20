Number = int(input("Please Enter any Number: "))
temp=Number
Reverse = 0
while(Number > 0):
    Reminder = Number %10
    Reverse = (Reverse *10) + Reminder
    Number = Number//10
if(temp==Reverse):
	print"yes"
else:
	print"no"
