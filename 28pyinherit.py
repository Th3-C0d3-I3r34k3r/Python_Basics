# Python Inheritance
print ()
print ("  ************************************")
print ("  *        Python INHERITANCE        *")
print ("  ************************************")
print ()
# Inheritance allows us to define class that inherits all the methods and properties from th eanother class
# ParentClass: class being inherited from , also caleed base class
# ChildClass: class that inherits from another class, also caleed derived class
print ()
print (" CREATE A PARENT CLASS:")
print ("-----------------------")
print ()
# Create class named Person , with firstname and lastname properties ,and a print name method
class Person:
	def _init_(self, fname,lname):
		self.fname = fname
		self.lname = lname

	def printname(self):
		print(self.fname, self.lname)

# Use the Person class to create an object, and then execute the printname method		
x = Person("John", 36)
x.print()
print ()
print (" CREATE A CHILD CLASS:")
print ("----------------------")
print ()
# To create a class that inherits the functionality from another class send the [arrent class as a parammeter when creating the child class
# Create a class named stttudent which will inherit the properties and merthods from the person class
class (Person):
	pass # Use the pass keyword when u dont want to add anyother properties or methods to the class
x = Sttdent("Mike", "Olsen")
x.printname()
print ()
print (" Add the _init_ Function:")
print ("-------------------------")
print ()
# the _init_ function is called automatically every time the object is being used to create anew object
class Student(Person):
	def _init_(self, fname, lname):
		# add properties etc
# To keep the inheritance of parent's _init_() function add a call to parent _init_() functionn



