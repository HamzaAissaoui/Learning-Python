'''Using type , str , dir , and Other Built-In Functions'''

# 1. Type function:
>>> li = []
>>> type(li)										#Output: <type 'list'>

>>> import odbchelper
>>> type(odbchelper) 								#Output: <type 'module'>

>>> import types
>>> type(odbchelper) == types.ModuleType			#Output: True

# 2. Str function:

>>> horsemen = ['war', 'pestilence', 'famine']
>>> str(horsemen)									#Output: "['war', 'pestilence', 'famine']"

>>> str(odbchelper) 								#Output: "<module 'odbchelper' from 
													#'c:\\docbook\\dip\\py\\odbchelper.py'>"

>>> str(None)										#Output: 'None'

#3. dir function:

>>> li = []
>>> dir(li) #Output: ['append', 'count', 'extend', 'index', 'insert','pop', 'remove', 'reverse', 'sort']

>>> d = {}
>>> dir(d)  #Output: ['clear', 'copy', 'get', 'has_key', 'items', 'keys', 'setdefault', 'update', 'values']

>>> import odbchelper
>>> dir(odbchelper)  #Output: ['__builtins__', '__doc__', '__file__', '__name__', 'buildConnectionString']

#4. callable function:

>>> import string
>>> string.punctuation 							#Output: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

>>> string.join 								#Output: <function join at 00C55A7C>

>>> callable(string.punctuation) 			
False

>>> callable(string.join)
True

#5. getattr function:

>>> li = ["Larry", "Curly"]
>>> li.pop									#Output: <built-in method pop of list object at 010DF884>

>>> getattr(li, "pop")						#Output: <built-in method pop of list object at 010DF884>

>>> getattr(li, "append")("Moe") 
>>> li
["Larry", "Curly", "Moe"]

>>> getattr({}, "clear")					#Output: <built-in method clear of dictionary object at 00F113D4>

>>> getattr((), "pop")
"""
Traceback (innermost last):
File "<interactive input>", line 1, in ?
AttributeError: 'tuple' object has no attribute 'pop' """

#6. getattr on modules:

>>> object = odbchelper
>>> method = "buildConnectionString"

>>> getattr(object, method)						#Output: <function buildConnectionString at 00D18DD4>

>>> type(getattr(object, method))				#Output: <type 'function'>

>>> import types
>>> type(getattr(object, method)) == types.FunctionType	#Output: True

>>> callable(getattr(object, method))					#Output: True

