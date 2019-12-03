#1. List filtering:

>>> li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]

>>> [elem for elem in li if len(elem) > 1]				 #Output: ['mpilgrim', 'foo']

>>> [elem for elem in li if elem != "b"]				 #Output: ['a', 'mpilgrim', 'foo', 'c', 'd', 'd']

>>> [elem for elem in li if li.count(elem) == 1] 		 #Output: ['a', 'mpilgrim', 'foo', 'c']

#2. AND :

>>> 'a' and 'b' and 'c'
'c'#the and returns the last true value

>>> '' and 'b'
''#the and returns the first false value

#3. OR: 

>>> 'a' or 'b'
'a'#or returns the first true value

>>> '' or [] or {}
{}#or returns the last false value


#4. the and-or Trick:

>>> a = "first"
>>> b = "second"

>>> 1 and a or b 
'first'	#'1' is true, it returns a

>>> 0 and a or b
'second'#'0' is false, it returns b

#5. Using the and-or Trick Safely
>>> a = ""
>>> b = "second"

>>> (1 and [a] or [b])[0]				#Output: ''

#6. lambda function:

>>> g = lambda x: x*2
>>> g(3)								#Output: 6

>>> (lambda x: x*2)(3)				#Output: 6

Example:

>>> processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)

