#Python RegEx
print ()
print ("  *****************************")
print ("  *      Python RegEx         *")
print ("  *****************************")
print ()
print ()
print("Regex, or RegularExpression is a sequence of characters that forms a search pattern")
print("it can be used to check if a string contains the specified search pattern")
print()
print("RegEx Module:")
print("*************")
print()
print("To use the regex use the mocule called : ' re '")
print()
print("RegEx Module:")
print("*************")
print()
import re
txt = "The rain in spain"
x = re.search("^The.*Spain$", txt)
print(x)
print()
print("Find all() Function:")
print("********************")
print()
print("findall() : It returns list containing all the matches ")
print()
import re 
str = "The rain in spain"
x = re.findall("ai", str)
print(x)
print("If no match was found, It returns an empty  list ")
print()
print()
import re

str = "The rain spain"
x = re.findall("portugal", str)
print(x)
print()
print("Search() Function:")
print("********************")
print()

import re
str = "The rain in spain"
x = re.search("\s", str)
print(x)

print("The first white-space charatcter ios located in position", x.start())
print()
print("Split() Function:")
print("********************")
print()
print("split() : it returns a list where the string has been split at each match")

import re
str = "The rain in spain"
x = re.split("\s", str)
print(x)

print("maxsplit() : can control the no.of.occurances")

import re
str = "The rain in spain"
x = re.split("\s", str, 1)
print(x)
print()
print("Sub() Function:")
print("***************")
print()
print("sub() : replace the matches with the text of your choice")

import re
str = "The rain spain"
x = re.sub("\s", "9", str)
print(x)

print("count parameter : we can control the no of replacements by specifyiny the count parametr")
import re
str = "The rain in spain"
x = re.sub("\s", "9", str, 2)
print(x)

print()
print("Match Object:")
print("*************")
print()
print("An object containiing info about the search and the result")

import re
str = "The rain spain"
x = re.search("ai", str)
print(x)
print("Print the poition [start and end position] of the first match occurance")
import re
str = "The rain Spain"
x = re.search("\bS\w+", str)
print(x.span())
print(x.string())
print(x.group())
