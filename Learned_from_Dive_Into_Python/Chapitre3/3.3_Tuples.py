""" This file contains all commands in chapter 3.3 Tuples: """

# 1. Defining a tuple:

t = ("a", "b", "mpilgrim", "z", "example")	#Notice the parentheses
t[0]	#Output: 'a'
t[-1]	#Output: 'example'
t[1:3]	#Output: ('b','mpilgrim')

# Notes:
	# 1. Tuples have no methods, except:
		"z" in t #Output: True

	# 2. Faster than lists and are uneditable.
	# 3. Safer, they "write-protect" data. 
	# 4. Can be used as keys in dictionaries.
	# 5. tuple freezes a list, and list thaws a tuple. 