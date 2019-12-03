"""This file contains all commands in chapter 3.4 Variables"""

# 1. Assigning multiple values at once:

v = ('a', 'b', 'e')
(x, y, z) = v 		#Output: x:'a', y:'b', z:'e'

# 2. Assigning Consecutive Values (Range)

(MONDAY, TUESDAY, WEDNESDAY) = range(3) #Output: MONDAY:0, TUESDAY:1, WEDNESDAY:2

#Parameters for range 
"range(start[,stop,step])\
			 OPTIONAL"

#	You can also use multi-variable assignment 
#	to build functions that return multiple values,