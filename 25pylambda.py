# PYTHON lambda function
# "lambda" function is small anonymous function, it can have no of args bt only one expression
print ()
print ("PYHON lambda")
print ("------------")
print ()
print ("Syntax:")
print ("-------")
print ("lambda arguments : expressions")
x = lambda a : a + 10
print (x(5))
print ()
print ("lambda funcn can take number of arguments:")
print ("------------------------------------------")
print ()
y = lambda a, b : a + b
print (y(10, 20))
print ()
print ()
z = lambda a, b, c : a + b + c
print (z(10, 20, 30))
print ()
print ()
def myfunc(n):
	return lambda a : a * n

mydoubler = myfunc(2)	
mytripler = myfunc(3)
print (mydoubler(11))
print (mytripler(11))