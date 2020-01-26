# python Functions
#Python Funstions is a block of code which runs when it is called
#We can pass parameters as data
#Function returns data s a result
print ()
print ("Creating a function")
print ("-------------------")
print ()   
#  function can be created using the 'def' function
 def my_function():
 	print ("Hello")
my_function() 	
print ()
print ("Calling a function")
print ("------------------")
print () 	
# To call a function use the function name followed by parenthesis,
def greetings():
	 print ("Welcome World!")
greetings()	
print ()
print ("Parameters")
print ("----------")
print ()  
# information can be passsed to functions as parameters
#Parameters are specified after the function nane, inside the parentheses
def our_func(fname):
	print(fname + "refsnes")

our_func("Emil")	
our_func("Tobias")
our_func("Linus")
print ()
print ("Default Parameters value")
print ("------------------------")
print ()
def tmp_function(country = "norway"):
	print ("I am from" + country)

tmp_function("india")	
tmp_function("america")
tmp_function() # if we call a function without parameter it will take the default value
print ()
print ("Passing List As Parameters")
print ("--------------------------")
print ()
# We can send any data type as parameters to a function (string, number, list, dictionary)
def data_function(food):
	for x in food:
		print(x)

fruits = ["apple", "orange", "banana"]
data_function(fruits)
print ()
print ("Return Value")
print ("------------")
print ()
# Let a function to return value, use return statemnt
def ret_function(x):
	return 5 * x
ret_function(2)	
ret_function(3)
print ()
print ("Recursion")
print ("---------")
print ()
# Recursion : a function can call itself
# 
def tri_recursion(k):
	if (k > 0):
		result = k + tri_recursion(k-1)
		print(result)
	else:
		result = 0
		return result
print ("\n\n Recursion Example Results")		
tri_recursion(6)
		

   