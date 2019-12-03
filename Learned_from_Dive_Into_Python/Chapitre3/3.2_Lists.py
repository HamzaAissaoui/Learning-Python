""" This file contains all commands in chapter 3.2 Lists: 
	1- Declaring a list
	2.1- Slicing a List
	2.2- Slicing Shorthand	
	3. Adding elements to a list
	4. Searching a list
	5. Removing elements from a list
	6. List operators
	"""

# 1- Declaring a list
li = ["a", "b", "mpilgrim", "z", "example"]
print (li) 		#Output: ['a', 'b', 'mpilgrim', 'z', 'example']
print (li[0])	#Output: a
print (li[-1])	#Output: example
				#Note:  think of it this way: 
				#		li[-n] == li[len(li) - n]
				#	 So	li[-3] == li[5 - 3] == li[2]

# 2.1- Slicing a List
print()
print (li[1:3])		#Output: ['b', 'mpilgrim']
print (li[1:-1])	#Output: ['b', 'mpilgrim', 'z']
print()

# 2.2- Slicing Shorthand

print(li[:3]) 		#Output: ['a', 'b', 'mpilgrim']
print(li[3:])		#Output: ['z', 'example']
					#Note:  li[:n] will always return the first n elements.
					#		li[n:] will return the rest, regardless of the length of the list.

# 3- Adding Elements to a List
li.append("new")				#Output: ['a', 'b', 'mpilgrim', 'z', 'example', 'new']
li.insert(2, "new")				#Output: ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new']
li.extend(["two", "elements"])	#Output: ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']

# 4- Searching a List
li.index("example")	#Output: 5
li.index("new")		#Output: 2
					#Note: Index finds the first occurence of the value.

"c" in li 			#Output: False 

# 5- Removing elements from a list

li.remove("z")		#Output: ['a', 'b', 'new', 'mpilgrim', 'example', 'new', 'two', 'elements']
li.remove("new")	#Output: ['a', 'b', mpilgrim', 'example', 'new', 'two', 'elements']
					#Note: 	 remove removes the first occurrence of a value from a list.

li.pop()			#Output: 'elements'
					#Note:	 pop() : #1. removes the last element of the list.
									 #2. returns the value that it removed.

# 6- List operators

li+= ["ines","hamza"] 	#Output: ['a', 'b', 'mpilgrim', 'example', 'new', 'two', 'ines', 'hamza']

numli = [1, 2] * 3		#Output: [1, 2, 1, 2, 1, 2]


