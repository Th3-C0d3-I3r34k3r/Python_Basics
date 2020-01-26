#Python MYSQL DATABASE
print ()
print ("  **********************************")
print ("  *     Python MYSQL DATABASE      *")
print ("  **********************************")
print ()
print ()
print ()
print("Creating a Database")
print("-------------------")
import mysql.connector
mydb = mysql.connector.connect(
  host = "localhost",
  user = "username",
  passwd = "passwd"
	)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")
print("Check if Database exists")
print("------------------------")
# we can check it by 'SHOW DATABASE'