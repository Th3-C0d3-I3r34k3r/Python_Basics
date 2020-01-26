print ()
print ("  ************************************")
print ("  *         Python ITERATORS         *")
print ("  ************************************")
print ()
print ()
print (" Python iterators:")
print ("------------------")
print ()
print("An iterator is an object that contain countable no of values")
print("Python iterator methods are: _iter_, _next_")
print ()
print (" Iterator vs Iterable:")
print ("----------------------")
print ()
print("Lists, Tuples, Dict, Sets are all iterable objects")
print ()
print (" Iter() Method:")
print ("---------------")
print ()
mytuple = ("apple", "orange", "Banana")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
print("Strings are also iterable objects and can return it an iterator")
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print ()
print (" Looping through an iterator:")
print ("-----------------------------")
print ()
print("We can also use for loop to iterate through an objects")
mytuple = ("apple", "orange", "banana")
for x in mytuple:
	print(x)
print("We can iterate through the characters")	
mystr = "banana"
for x in mystr:
	print(x)
print ()
print (" Create an iterator:")
print ("--------------------")
print ()	
print("To create an object/class as an iterator you have to implement the methods: _iter_, _next_ to your objects")
print("Create an iterator that rturns numbers, starting with1, and each sequence will increase by one")
class MyNumbers:
	def _iter_(self):
		self.a = 1
		return self

    def _next_(self):
        x = self.a
        self.a += 1		
        return x
myclass = MyNumbers()        
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print ()
print (" Stop an iterator:")
print ("------------------")
print ()
print("To prevent the iteration to go on forever, we can use the 'StopIteration' Statement")
print("Stop after 20 iteration")
class MyNumbers:
	def _iter_(self):
		self.a = 1
		return self

	def _next_(self):
		if self.a <= 20:
			x = self.a
			self.a += 1
			return x
		else:
		raise StopIteration
mycalss = MyNumbers()			
myiter = iter(myclass)

for x in myiter:
	print(x)