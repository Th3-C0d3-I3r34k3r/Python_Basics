# Python Datetime
print ()
print ("  *****************************")
print ("  *     Python DATETIME       *")
print ("  *****************************")
print ()
print ()
print (" PYTHON DATES:")
print ("--------------")
print ()
print("To use the date time function usew the 'datetime' module to work with objects")
print()
print()
import datetime

x = datetime.datetime.now()
print(x)
print ()
print ()
print (" DATE OUTPUT:")
print ("-------------")
print ()
print ()
print ()
print (" Return the year and name of week day:")
print ("--------------------------------------")
print ()
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
print ()
print ()
print (" Create Date Objects:")
print ("---------------------")
print ()
import datetime

x = datetime.datetime(2020, 5, 7)
print(x)
print ()
print ()
print (" The strftime() Method:")
print ("-----------------------")
print ()
print("The 'datetime' object methos converts date obj's into readable strings")
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))