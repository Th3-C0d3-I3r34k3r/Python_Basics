# Python for loop
# for loopp is used for iteraring over a sequence (a sequence may be a list, a dict, a tuple, a set)
print ()
print ("For loop")
print ("------------")
print ()
fruits = ["apple", "orange", "cherry"]
for x in fruits:
	print(x)
# for loop does not require an indexing variable to set beforehand
print ()
print ("looping through a string")
print ("------------------------")
print ()
for x in "banana":
	print(x)
print ()
print ("The Break Statement")
print ("-------------------")
print ()	
fruit = ["apple", "orange", "mango"]
for x in fruit:
	print (x)
	if x == "orange":
	 break
fruit1 = ["apple", "orange", "banana"]	 
for x in fruit1:
	if x=="banana":
	    break
	print (x)
print ()
print ("The Continue Statement")
print ("----------------------")
print ()
# We can stop the current iteration and continue to the next
fruit2 = ["apple", "orange", "banana"]
for x in fruit2:
    if x == "banana":
    	continue
    print(x)
print ()
print ("The range() Statement")
print ("---------------------")
print ()    
# Loop through a set of code a specigfic no of times , we can use range() function
# range() function returns a sequence numbers starting from 0 by default and increment by 1
for x in range(6):
	print(x)
print("***********************************")	
# We  can also give the increment value 
for x in range(0, 20, 2):
	print(x)
print("***********************************")	
# We can also give the starting poibnt and ending point
for c in range(2, 20):
	print (c)
print ()
print ("The else in for loop")
print ("---------------------")
print ()  	
# else keyword in for loop specifies a block of code to be  executed when th eloop is finished
for x in range(6):
	print(x)
else:
    print("finally Finished")	
print ()
print ("The Nested loop")
print ("---------------")
print ()    
#loop inside a loop
# inner loop will beexeuted one time for each iteration of the outer loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
	for y in fruits:
		print(x,y)