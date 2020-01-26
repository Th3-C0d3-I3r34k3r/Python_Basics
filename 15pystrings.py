#PythonStrings
#Use Qotatio marks to denote the Strings
#  for Eg: 'hello' "Hello"
a = "Hello, World!"
# Get the pareticular letter using indexing
print(a[0])
# To Get continuous chars
print(a[0:5])
#Strippingf the white sapcwe using the srip method
print(a.strip())
#Another Stripping Example
b = " i Love India "
print (b.strip())
#Calculate the langth of the String
print (len(a))
#convert lower to higher
print (a.lower())
#Convert higher to lower
print (a.upper())
#String Replace a string with another string
print (a.replace("World", "Baby"))
#Pythonb Split method
c = "I Love India Very Much!"
print (c.split(" "))
#Command Line String Input
print ("*****************************")
print ("*****************************")
print ("*****************************")
#Getting User input
print ("Getting User Input")
print ("Please Enter a number....?")
inpt = input()
print (inpt)

print ("Printing the usr name")
print ("Enter Your User Name.........")
usrname = input()
print ("Welcome,", usrname)