"""Commands to remember:

1. re.findall(pattern, text): returns a list containing all occurences of pattern in text

2. re.findall(pattern(grp1)(grp2)(grp3)..,text): returns a list of tuples, each element of the list contains 
												the occurence of the pattern and each tuple contains the groups
												of the pattern

3. re.findall(pattern, text, [optional argument]): we can add optional arguments

"""
import re
 
#1. re.findall:

>>> re.findall(r'[\w.]+@[\w.]+','blah hamza.a@gmail.com tomasmiller@hotmail.com  blah')
['hamza.a@gmail.com', 'tomasmiller@hotmail.com']

>>> re.findall(r'([\w.]+)@([\w.]+)','blah hamza.a@gmail.com tomasmiller@hotmail.com  blah')
[('hamza.a', 'gmail.com'), ('tomasmiller', 'hotmail.com')]


>>> re.findall(r'[\w.]+@[\w.]+','blah hamza.a@Gmail.com tomasmiller@hotmail.com  blah', re.IGNORECASE)
['hamza.a@Gmail.com', 'tomasmiller@hotmail.com']
