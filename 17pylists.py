#Python Lists
# 4 types of DATA collection in python
# LIST [] , TUPLE () , SET {} , DICTIONARY { KEY:VALUE , KEY:VALUE }
print ()
print ("  ****************************")
print ("  *      Pythyon LISTS       *")
print ("  ****************************")
print ()
# LISTS -> Ordered , Changable Allows Duplicate Members
# Python LISTS are written in square brackets[]
thislist = ["apple", "orange" , "banana" ]
print (thislist)
print ()
print ("*----------------------------------------------------------------------*")
print (" Note:We can access the contents of the list by reffering its index num")
print ("*----------------------------------------------------------------------*")
print ("index place[0] : " , thislist[0])
print ("index place[1] : " , thislist[1])
print ("index place[2] : " , thislist[2])
print ("*----------------------------------------------------------*")
print (" Note: We can change the value of lists by its index number")
print ("*----------------------------------------------------------*")
mylist = ["book", "pencil", "pen"]
mylist[0] = "BKDeleted"
print (mylist)
mylist[1] = "PencilDeleted"
print (mylist)
mylist[2] = "PenDeleted"
print (mylist)
print ()
print ()
print ("LOOPING THROUGH THE LIST:")
print ("-------------------------")
# Print all items in the list items
favlist = ["1", "2", "3", "4", "5"]
for x in favlist:
  print (x)
myfav = ["curd", "briyani", "barota"]
for x in myfav:
	print (x)
print ()
print ("CHECKINGF FOR ITEMS IN THE LIST:")
print ("--------------------------------")
print ()
flist = ["jan", "feb", "mar", "apr", "may"]
print (flist)
print ()
if "jan" in flist:
	print ("Huh!, jan is presented in the list")
print ()
print ("CHECKINGF FOR LENGTH OF THE LIST[ len() ]:")
print ("------------------------------------------")
print ()
lenlist = ["one", "two", "three", "four"]
print ("The length of the list is:", len(lenlist))
print ()
print ("ADD ITEMS IN THE LIST[ append() ]:")
print ("----------------------")
print ()
addlist = ["one", "two",]
addlist.append("THREE")
print (addlist)
print ()
print ("ADD ITEMS IN SPECIFIED INDEX IN THE LIST[ insert() ]:")
print ("-----------------------------------------------------")
print ()
addlist.insert(0, "ZERO")
print (addlist)
print ()
print ("REMOVE ITEMS IN THE LIST[ remove() ]:")
print ("-------------------------------------")
print ()
remlist = ["apple", "banana", "catch", "donkey"]
remlist.remove("banana")
print (remlist)
print ("'banana' is successsfully removed!")
print ()
print ("REMOVE ITEMS IN THE LIST[ pop() ]:")
print ("----------------------------------")
print ("*-----------------------------------------------------------------------*")
print ("*Note: if index are not specified means last item in the list is deleted*")
print ("*-----------------------------------------------------------------------*")
poplist = ["donkey", "monkey", "horse", "lion"]
print (poplist)
poplist.pop()
print(poplist)
poplist.pop(1)
print (poplist)
print ()
print ("REMOVE ITEMS IN THE LIST[ del() ]:")
print ("----------------------------------")
print()
dellist = ["one", "two", "three", "four"]
print (dellist)
del dellist[0]
print (dellist)
print ("*----------------------------------------------------------------------------*")
print ("* If index is not specified in del() function the list  is completely deleted*")
print ("*----------------------------------------------------------------------------*")
del dellist
print ("The dellist ic completely removed!")
print ()
print ("CLEAR ITEMS IN THE LIST[ clear() ]:")
print ("-----------------------------------")
print()
clrlist = ["apple", "orange", "banana"]
print (clrlist)
# Deletes every content in the list
clrlist.clear()
print (clrlist)
print(len(clrlist))
print ()
print ("COPY ITEMS IN THE LIST[ copy() ]:")
print ("-----------------------------------")
print()
implist = ["addr1", "addr2", "addr3", "addr4"]
print ("  Real implist contents:", implist)
print ()
tmplist = implist.copy()
print ("Copied tmplist contents:", tmplist)
print ()
print ("COPY ITEMS IN THE LIST[ list() ]:")
print ("-----------------------------------")
print()
cpylist = ["one", "two", "three", "four", "five"]
print (cpylist)
cplist1 = list(cpylist)
print (cplist1)
print ()
print ("CREATE ITEMS IN THE LIST[ list() ]:")
print ("-----------------------------------")
print()
# to vreate the list using the list() construction use double braces list(("x","y","z",))
tmplist = list(("apple", "orange", "banana", "mango"))
print(tmplist)
print ()
print ("[ LIST METHODS ]:")
print ("---------------")
print()
# LIST METHODS: append(), clear(), copy(), count(), extend(), index(), insert(), pop(), remove(), reverse(), sort()
print ("# LIST METHODS: append(), clear(), copy(), count(), extend(), index(), insert(), pop(), remove(), reverse(), sort()")