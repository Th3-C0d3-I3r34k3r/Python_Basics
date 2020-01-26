# Python JSON
print ()
print ("  *****************************")
print ("  *       Python JSON         *")
print ("  *****************************")
print ()
print ()
print("JSON: syntax for storing and exchanging data")
print()
print("JSON: text written with JS object notation")
print ()
print (" JSON in Python")
print ("-------------")
print ()
print ()
print("Python has a built n function called json, which can be worked with JSON data")
print()
print ("Module_name: import json")
print()
print()
print("Parse JSON- Convert JSON TO  PYTHON")
print("PYTHON JSON HAVE THE METHOD:  json.loads() results in python Dictionary ")
import json
#some JSON
x = '{"name":"john", "age":30, "city":"NewYork"}'
# parse X
y = json.loads(x)
#the result is a python dictionary
print(y["age"])
print()
print()
print("Parse JSON- Convert PYTHON TO JSON")
print("PYTHON JSON HAVE THE METHOD:  json.dumps() ")
import json
# a python object(dict)
x = {
	"name": "baby",
	"age":25,
	"city":"NewYork"
}

#convert into JSON
y = json.dumps(x)

#the result is a JSON string
print(y)
print ()
print (" We can convert python objects into JSON strings")
print ("------------------------------------------------")
print ()
print ()
print("dict")
print("list")
print("tuple")
print("string")
print("int")
print("float")
print("true")
print("false")
print("None")
print ()
print (" convert python objects into JSON strings")
print ("-----------------------------------------")
print ()
print ()
import json

print(json.dumps({"name":"john", "age":25}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(["apple", "bananas"]))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print ()
print ()
print (" convert python into JSON ")
print ("--------------------------")
print ()
print ()
import json

x = {
	"name": "john",
	"age": 25,
	"married": True,
	"Divorced": False,
	"children": ("ann", "billy"),
	"cars": [
	{"model": "BMW 230", "mpg": 27.5},
	{"model": "FordEdge", "mpg": 24.1}

	]
}
# indent method is used to make the data as the readable form
print(json.dumps(x, indent=4))
# We can also use the seperators to change the defalut parameter
# print(json.dumps(x, indent=4, seperator=(".","+")))
print(json.dumps(x, indent=4, sort_keys=True))