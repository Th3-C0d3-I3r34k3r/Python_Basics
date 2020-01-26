# Python File Write
print ()
print ("  ******************************")
print ("  *     Python File Write      *")
print ("  ******************************")
print ()
print ()
print () 
print (" Write an existing File:")
print ("------------------------")
print ()
# To write to an existing file, you must add the open() parameter function
# "a" - Append   added at the end of the file
# "w" - Write  will over write any existing content
f = open("demotxt.txt", "a")
f.write("The appended text")
f.close()

# Open and read the file after the appending

f = open("demotxt.txt", "r")
print(f.read())
print ()
print () 
f = open("demotxt.txt", "w")
f.write("Woops! i have deleted all the content")
f.close()

# open and read the file after the apppending:
f = open("demotxt.txt", "r")
print(f.read())
# 'w' method will rewritew the entire file
