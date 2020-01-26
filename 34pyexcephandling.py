#Python Try Except
 # try = this block lets you to test ablock of code for errors
 # except = this block lets you to handle errors
 # finally = this block lets you to ececute code,regardless of the result of the try=and except blocks
print ()
print ("  **************************************")
print ("  *      Python Python Try-Except      *")
print ("  **************************************")
print ()
print () 
print (" PYTHON EXCEPTION HANDLING:")
print ("---------------------------")
print ()
try:
	print(x)
except:
	print("an exception occured")

# print(x)	 // Produces an error
print ()
print () 
print (" PYTHON MANY EXCEPTION:")
print ("-----------------------")
print ()
try:
	print(x)
except NameError:
    print("Variable x is not defined")	
except:
    print("Something else went wrong")    
print ()
print () 
print (" PYTHON ELSE:")
print ("-------------")
print ()
print("else:  - A block of code to be executed iof no errors were occured")
try:
	print("Helo")
except:
    print("Something wqent wrong")	
else:
    print("Nothing Went wrong")    
    print ()
print () 
print (" PYTHON FINALLY:")
print ("----------------")
print ()
print("finally: - it will be executed if the try block raises san error or not")
try:
	print(x)
except:
    print("Something went wrong")	
finally:
    print("Both try and except executed successfully") 
print()
print()
print("AnotherExample:")       
print()
try:
	f = open("demofile.txt")
	f.write("lorumIpsum")
except:
   print("Something weent wrong when writing the file")	
finally:
   f.close()   


