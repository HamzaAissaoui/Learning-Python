"""	This file contains all commands in chapter 3.1 Dictionaries:
	 1- declaring a dictionary 
	 2- getting values using keys 
	 3.1- modifying items
	 3.2- adding new key-value items
	 4- deleting items"""

# 1- Declaring a dictionary
d = {"server":"mpilgrim", "database":"master"}
print(d)

# 2- Finding a value using a key (you can't go the other way)
print d["server"]	#Output: 'mpilgrim'

# 3.1- Modifying a Dictionary

d["database"] = "pubs"
print d 	#Output: {'server': 'mpilgrim', 'database': 'pubs'}

# 3.2- Adding a new element
d["uid"] = "sa" 
print d     #Output: {'server': 'mpilgrim', 'uid': 'sa', 'database': 'pubs'} 
			
			#Note:  Python is case sensitive, so if you try to modify d["uid"] and you type d["UId"],
			# 		python will create a new element

# 3.3- Mixing Datatypes in python
d["retrycount"] = 3
d[42] = "douglas"

print d 	#Output: {'retrycount': 3, 42: 'douglas', 'database': 'pubs', 'uid': 'sa', 'server': 'mpilgrim'}

# 4- Deleting from a Dictionary
del d[42]	#Output: {'retrycount': 3, 'database': 'pubs', 'uid': 'sa', 'server': 'mpilgrim'}
d.clear() 	#Output: {}

