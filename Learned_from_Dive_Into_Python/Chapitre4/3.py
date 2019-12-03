#1. split With No Arguments:

>>> s = "this	is\na\ttest"

>>> print s 							#Output: this	is
										#		 a 	test


>>> print s.split()						#Output: ['this', 'is', 'a', 'test']


>>> print " ".join(s.split())			#Output: 'this is a test'

#2. ljust:

>>> s = 'buildConnectionString'

>>> s.ljust(30) 
'buildConnectionString			'	#so it adjusts the string to 30 characters

>>> s.ljust(20) 
'buildConnectionString'

#3. Printing a list:

>>> li = ['a', 'b', 'c']
>>> print "\n".join(li) 
a
b
c

