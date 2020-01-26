#Python delete file
print ()
print ("  ******************************")
print ("  *     Python Deletefile      *")
print ("  ******************************")
print ()
print ()
print () 
print("Delete  a file:")
print("---------------")
print("To delete a file must import os.remove() function")
import os
os.remove("demotxt.txt")
print()
print()
print("To avoid getting an error , check the fileexixts opr not:")
import os
if os.path.exists ("demotxt.txt"):
 	os.remove("demo1txt.txt")
else:
 	print("The file doesnt exist")
print ()
print () 
print("Delete  a folder:")
print("-----------------")
print("To delete an entire folder use os.rmdir() method")
import os
os.rmdir("myfolder")
#This only can remove the empty folders