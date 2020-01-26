# Python Dictionary
# Python Dictioinary set using ' { } ' symbol
# They are UnOrdered , Changeable, Indexed
# They are written in key value pairs [  key:value  ]
print ()
print ("  ********************************")
print ("  *      Python DICTIONARY       *")
print ("  ********************************")
print ()
thisdict = {
	"name" : "baby",
	"age" : 25,
	"gender": "male"
	}
print (thisdict)
print()
print()
print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print()
print()
print ()
print (" ACCESS ITEMS:")
print ("--------------")
print ()	
print ("*------------------------------------------------------------------------------*")
print ("* NOTE: We can Access the item in DICT by using its key names inide square brackets *")
print ("*------------------------------------------------------------------------------*")
print () 
x = thisdict["name"]
print(x)
# theres also called another method [    get()    ]
a = thisdict.get("age")
print (a)
print()
print()
print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print()
print()
print ()
print (" CHANGE VALUES:")
print ("---------------")
print ()	
print ("*-------------------------------------------------------------*")
print ("* NOTE: We can Change the item in DICT by using its key names *")
print ("*-------------------------------------------------------------*")
print () 
accdict = {
	"name":"ford",
	"fuel":"50litres",
	"mileage":"10kmpl",
	"price":"10lakhs",
	"year":2019
}
# change year as 2015
accdict["year"] = 2015
print (accdict)
print()
print()
print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print()
print()
print ()
print (" LOOPING THROUGH A DICTIONARY:")
print ("------------------------------")
print ()
mydict = {
	"name":"ford",
	"fuel":"50litres",
	"mileage":"10kmpl",
	"price":"10lakhs",
	"year":2019
}
for c in mydict:
	print (mydict[c])

# you can alsu use [ values()	] function to return the values of the dictionary
print()
print()
mdict = {
	"name":"ford",
	"fuel":"50litres",
	"mileage":"10kmpl",
	"price":"10lakhs",
	"year":2019
}
for x in mdict.values():
	print (x)

# To display both the values and the key use items()	function
print()
print()
adict = {
	"name":"ford",
	"fuel":"50litres",
	"mileage":"10kmpl",
	"price":"10lakhs",
	"year":2019
}
for s in adict.items() :
	print(s)
print ()
print (" CHECK IF KEY EXISTS:")
print ("---------------------")
print ()
print ()	
print ("*-----------------------------------------------------------------------------*")
print ("* NOTE: To determine the if a specified key in a dictionary, use in  keyword  *")
print ("*-----------------------------------------------------------------------------*")
print () 
sdict = {
	"name":"ford",
	"fuel":"50litres",
	"mileage":"10kmpl",
	"price":"10lakhs",
	"year":2019
}
if "fuel" in sdict:
	print("Yes 'fuel' key exists")
print ()
print ("DICTIONARY length:")
print ("------------------")
print ()	
print(len(sdict))
print ()
print ("ADDING ITEMS:")
print ("-------------")
print ()
ndict = {
	"name":"ford",
	"fuel":"50litres",
	"mileage":"10kmpl",
	"price":"10lakhs",
	"year":2019
}
ndict["rating"] = "*****"
print (ndict)
print ()
print ("REMOVING ITEMS:")
print ("-------------")
print ()
# Remove the items using the pop method
ndict.pop("rating")
print (ndict)
print ()
print ("REMOVING ITEMS Randomly (use 'popitem()' function):")
print ("---------------------------------------------------")
print ()
ndict.popitem()
print(ndict)
print ()	
print ("*-------------------------------------------------------*")
print ("* NOTE: To delete a specified key use the keyword: del  *")
print ("*-------------------------------------------------------*")
print () 
tdict = {
	"name":"ford",
	"fuel":"50litres",
	"mileage":"10kmpl",
	"price":"10lakhs",
	"year":2019
}
del tdict["mileage"]
print(tdict)
# To delete the dictionary completely use del keyword withoua any argument


'''tdict = {
	"name":"ford",
	"fuel":"50litres",
	"mileage":"10kmpl",  # this will raise an error
	"price":"10lakhs",
	"year":2019
}
del tdict
print(tdict) '''


print ()
print (" CLEARING THE DICTIONARY USING THE clear() function")
print ("---------------------------------------------------")
print ()
clrdict = {
	"name":"ford",
	"fuel":"50litres",
	"mileage":"10kmpl",  # this will raise an error
	"price":"10lakhs",
	"year":2019
}
print (clrdict)
clrdict.clear()
print (clrdict)
print ("dictionary Emptied...!")
print ()
print (" COPYING THE DICTIONARY USING THE copy() function")
print ("---------------------------------------------------")
print ()
cpydict = {
	"name":"ford",
	"fuel":"50litres",
	"mileage":"10kmpl",  
	"price":"10lakhs",
	"year":2019
}
realdict = cpydict.copy()
print (realdict)

# ' list() ' method can also used to copy the dictionary
print ()
print (" COPYING THE DICTIONARY USING THE dict() function")
print ("---------------------------------------------------")
print ()
fakedict = {
	"name":"ford",
	"fuel":"50litres",
	"mileage":"10kmpl", 
	"price":"10lakhs",
	"year":2019
}
truedict = dict(fakedict)
print ("TrueDict Is:")
print (truedict)
print ()
print (" CREATING  THE DICTIONARY USING THE dict() Constructor")
print ("---------------------------------------------------")
print ()
xdict = dict(brand="tesla", year=2019, mpl= "kms")
print (xdict)
print ()
print (" DICTIONARY METHODS:")
print ("--------------------")
print ()
print ("clear(), copy(), fromkeys(), get(), items()")
print ("keys(), pop(), popitem(), setdefault(), update()")
print ("update(), values()")

