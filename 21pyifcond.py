# Python  if-Else Condition Statement
#  EQUALS == , BOT EQULS !== , LESS THAN < , GREATER THAN > , 
#  GREATER THAN OR EQUAL TO >= , LESS THA OR EQUAL TO <= , 
# if-STATEMENT
a = 33
b = 200
if b > a:
	print("B greater thsn A")
 # Give importance to indentation  when using the condition statements	
'''
#-------> Produces an error <----------#mg
#a = 33
#b = 200
#if b > a:
#print("B greater thsn A") #(beacuse no indentation is left here)

 # Elif Statement
 print ()
 '''
print ()
print ("Elif Statement")
print ("--------------")
print ()
a = 33
b = 33
if b > a:
	print ("b is geater than a" )
elif a == b:
	print ("Value of A and B are Same")
print ()
print ("Else Statement")
print ("--------------")
print ()
a = 300
b = 33
if b > a: 
	print ("B is Greater Than A")
elif a == b:	
	print ("A and B are Equal")
else:
	print ("A is Greater Than B")
print ()
print ("Else without elif Statement")
print ("---------------------------")
print ()	
a = 200
b= 33
if b  > a:
	print ("b is greater than a")
else:
    print ("b is not greater tahn a")	
print ()
print ("ShortHanf if Statement")
print ("----------------------")
print ()
# if we have only one statemnt to execute , you can put it in the same line as the if statement
a = 50
b = 20
if a > b: print("a is graeater than b")
# if given condition fails nothing will displayed as output
print ()
print ("ShortHanf if-else Statement")
print ("---------------------------")
print ()
a = 10 
b = 20
print (" A ") if a > b else print ("B")
#-----------------------------------------------------------
# WE CAN ALSO HAVE MULTIPLE SET OF ELEMENTS ON THE SAME LINE
#-----------------------------------------------------------
print ("One line if-else statemnt  with 3 Conditions")
print ("--------------------------------------------")
a = 50
b = 10
print ("A") if a > b else print ("B") if b > a else print ("=")
print ()
print (" AND Keyword")
print ("------------")
print ()
# AND is alogical operator and used to combine conditional satements
a = 10 
b = 20
c = 33
# Displays O/P if both the conditions are true
if a < c and b < c:
	print ("Both the conditions are true")
print ()
print (" OR Keyword")
print ("------------")
print ()	
a = 10 
b = 20
c = 33
# Displays O/P if both the conditions are true
if a < c or b > c:
	print ("Any one conditions are true")














