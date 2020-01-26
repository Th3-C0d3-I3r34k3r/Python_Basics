#Python Operators
# 1)Python Arithmetic operator

print ()
print ("  *****************************")
print ("  *  i)Arithmetic Operators   *")
print ("  *****************************")
x = 10
y = 5
#Addition
z = x+y
print (z)
#Subtraction
z = x-y
print (z)
#Multiplication
z = x*y
print (z)
#Division
z = x/y
print (int(z))
#Modulous
z = x%y
print(z)
#Exponentiation
z = x**y
print(z)
#FloorDivision
z = x//y 
print (z)
print ()
print ()
print ()
print ("***************************")
print ()
print ("  *****************************")
print ("  * ii)Assignment Operators   *")
print ("  *****************************")
# = Operator
num = 5
mystr = "mystring"
print (num)
print (mystr)
# += Operator
num += 3 # Abbreviates num = num + 3
# -= Operator
print (num)
num -= 3
print (num) # Abbreviates num = num - 3
# *= Operator
num *= 3
print (num)
# /= Operator
num /= 3
print (num)
# %= Operator
num %= 3 
print (num)
# //= Operator
num1 = 5
num1 //= 3
print (num1)
# **= Operator
num2 = 5
num2 **= 3
print (num2)
# &= Operator
num3 = 5
num3 &= 3
print (num3)
# |= Operator
num4 = 5
num4 |= 3
print (num4)
# ^= Operator
num5 = 5
num5 ^= 3
print (num5)
# >>= Operator
num6 = 5
num6 >>= 3
print (num6)
# <<= Operator
num7 = 5
num7 <<= 3
print (num7)
print ()

print ("***************************")
print ()
print ("  ****************************")
print ("  * iii)Comparison Operators *")
print ("  ****************************")
print ()
# == Comparison Operator

a = 10
b = 10
print (a == b) # o/p: true
print (a != b) # o/p: false
print (a>b) # o/p: false
print (a<b) # o/p: false
print (a<=b) # o/p: true
print (a>=b) # o/p: true
print ()
print ("***************************")
print ()
print ("  ****************************")
print ("  *  iv) Logical Operators   *")
print ("  ****************************")
print ()
c = 5
print ("Logical 'AND' Operator:")
print ( c>3 and c<2)
print ( c>4 and c<10)
print ("Logical 'OR' Operator:")
print ( c>10 or c<2)
print ( c>4 or c<10)
print ("Logical 'NOT' Operator:") # True means False  && False means True
print (not(c>10 or c<2))
print (not(c>4 or c<10))
print ()
print ("***************************")
print ()
print ("  ****************************")
print ("  *  v) Identity Operators   *")
print ("  ****************************")
print ()
# Identity Operatores are used to compare objects
d = ["apple", "banana"]
e = ["apple", "banana"]
f = d
print (f is d)
print (f is not d)
print ()
print ("***************************")
print ()
print ("  ****************************")
print ("  * vi) Membership Operators *")
print ("  ****************************")
print ()
print("Membership Operators are used to test if a sequence is present ia an object.")
g = ["banana", "apple"]
print ("banana" in g)
print ("mango" not in g)
print ("banana" not in g)
print ()
print ("***************************")
print ()
print ("  ****************************")
print ("  *  vii) Bitwise Operators  *")
print ("  ****************************")
print ()
#Used to compare(binary) numbers























