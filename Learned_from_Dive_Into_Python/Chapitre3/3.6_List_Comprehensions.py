"""Contains:
1. List Comprehensions
2. Joining lists of strings
3. Splitting strings into lists
"""

# 1. List Comprehensions

li = [1, 9, 8, 4] 
[elem*2 for elem in li]	#Output: [2, 18, 16, 8]
						#Note: 	li is still li = [1, 9, 8, 4], it is not modified.

li = [elem*2 for elem in li]	#Output: [2, 18, 16, 8]
								#Note: here li is modified.


# 2. The buildConnectionString function that we declared in Chapter 2

params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
params.keys()			#Output: ['server', 'uid', 'database', 'pwd']		#Notice it's not ordered.
params.values()			#Output: ['mpilgrim', 'sa', 'master', 'secret']
params.items()			#Output: [('server', 'mpilgrim'), ('uid', 'sa'), ('database', 'master'), ('pwd', 'secret')]
						#Notice: 'items' returns a list of tuples of the form (key, value).

[k for k, v in params.items()]	#Output: ['server', 'uid', 'database', 'pwd']
[v for k, v in params.items()]	#Output: ['mpilgrim', 'sa', 'master', 'secret']

["%s=%s" % (k, v) for k, v in params.items()] 
								#Output: ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']

# 3. Joining lists of strings

";".join(["%s=%s" % (k, v) for k, v in params.items()])	
								#Output: 'server=mpilgrim;uid=sa;database=master;pwd=secret'
								#Note:Joining a list that has non-strings will raise an exception.
# 4. Splitting strings into lists

li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']

s = ";".join(li)				#Output: 'server=mpilgrim;uid=sa;database=master;pwd=secret'

s.split(";")					#Output: ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']

s.split(";", 1)					#Output: ['server=mpilgrim', 'uid=sa;database=master;pwd=secret']