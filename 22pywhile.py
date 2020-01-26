# Python Loops
# two loops : i) While loops ii)For loops
print ()
print (" While Loops")
print ("------------")
print ()
# Executes  when the condition is true
# print i as long as i less than 6
i = 1
while i < 6:
	print (i)
	i += 1
print("***********************************")
print ()
print (" Break Statement")
print ("------------")
print ()
# it exits the loop eve n if the condition is true
i = 1
while i < 6:
	print(i)
	if i == 3:
		break
	i += 1
print("***********************************")
print ()
print (" Continue")
print ("------------")
print ()	
# 'Continue' stmt cn stop the current iteration and continue with the next
# continue to the nxt iteration if i is 3
i = 0
while i < 6:
	i += 1
	if i == 3:
		continue
	print (i)	