# Python Sets
# Unordered and Unindexed
# Written in curly brackets {}
print ()
print ("  *****************************")
print ("  *        Python SETS        *")
print ("  *****************************")
print ()
thisset = {"apple", "orange", "banana"}
print (thisset)
print ()
print ("*-----------------------------------------------------------------------------*")
print (" NOTE:Since SETS Are unordered it wil appear random in every time of execution ")
print ("*-----------------------------------------------------------------------------*")
print ()
print ()
print ("*------------------------------------------------------------------------*")
print (" NOTE: Since SETS Are unordered, We cant access SETS items by index number")
print ("*------------------------------------------------------------------------*")
print ()                  
print ()
print (" ACCESS ITEMS:")
print ("--------------")
print ()	
thisset = {"1", "2", "3", "4", "5"}
for x in thisset:
	print (x)
if "2"	in thisset:
	print (" '2' is fount")
print ()
print ("*-----------------------------------------------------------------*")
print (" NOTE: Once SETS Are created we cant change items but add new items")
print ("*-----------------------------------------------------------------*")
print ()
print ()
print (" ADD ITEMS TO SETS [ add() ]:")
print ("-----------------------------")
print ()
# For ADD a single entry use add() method
# To add multiple items use update() method
myset = {"apple", "orange"}
myset.add("banana")
print (myset)

# Addding multiple items in set
multiset = {"1","2","3"}
multiset.update("4","5")
print (multiset)
print (len(multiset))
print ()
print (" REMOVE ITEMS TO SETS [ remove(), discard() ]:")
print ("----------------------------------------------")
print ()
rmset = {"apple","orange", "mango"}
print (rmset)
rmset.remove("apple") # remove will raise an error if the item doesnot exist
print(rmset)
rmset.discard("orange") # discard() method doesnt raise an error
print (rmset)
popset = {"1", "2", "3", "4"}
print("Contents b4 pop: ", popset)
popset.pop()
print (popset)
print ()
print (" REMOVE ITEMS TO SETS [ clear() ] :")
print ("-----------------------------------")
print ()
clsset = {"1", "2", "3"}
d = clsset.clear()
print (d)
print ()
print (" REMOVE ITEMS TO SETS [ del() ] :")
print ("---------------------------------")
print ()
delset = {"l","o", "v", "e"}
print (delset)
del delset
#  print (delset)     // raise an error becoz it is deleted
print ()
print (" SET CONSTRUCTOR [ set() ] :")
print ("---------------------------------")
print ()
newset = set(("l", "j", "k"))
print (newset) # new set created
print ()
print (" SET METHODS :")
print ("--------------")
print ()
print ("add() , clear(), copy(), difference(), difference_update()")
print ("discard(), intersection(), intersection_update(), isdisjoint()")
print ("issubset(), pop(), remove(), symmetric_difference(), symmetric_difference_update()")
print ("union(), update() ")