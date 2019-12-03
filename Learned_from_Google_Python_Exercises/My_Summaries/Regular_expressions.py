"""Commands to remember:
0.import re: the module is necessary 're'

1. match= re.search(pattern, text): searching for the first occurence of that pattern in the text.

2. match.group(): returns the pattern if found

3. '.' in match means any character.

4. r'text': the 'r' before the text means in python that the interpreter should take 
			the text as it is and not take in consideration any special characters.

5. special characters:
	\. means search for a dot.
	\w means search for a word with number of \w characters so: \w\w\w means a word with 3 characters.
	\s means search for whitespace
	'+' means one or more of that thing, so \s+ means 1 or many whitespaces
	'*' means 0 or more of that thing, so \w* means 0 or more characters
	\S: non whitespace
	\S+: returns all characters before the first whitespace(even special ones, everything)

6. () groups: m= re.search(r'([\w.]+)@([\w.]+)','blah hamza.a@gmail.com  blah')
						   group(1)	  group(2)

7. 
"""

import re 
# 1. looking for pattern in text:

	#1.1.  When it exists:
	>>> match = re.search("iig","called piiig")#searching for iig in second paragraph

	>>> match
	<_sre.SRE_Match object at 0x7f597aa5d648>

	>>> match.group()
	'iig'

	#1.2. When it doesn't exist

	>>> match=re.search('igs','called piiig')
	>>> str(match)
	'none'
	#we can use the match as a boolean, so if it's there it won't be none, if it's not it'll be none.

#2. Working with re:

def Find(pat, text):
  match = re.search(pat, text)
  if match: print match.group()
  else: print 'not found' 

# 2.1. the dots:

>>> Find('...g','called piiig')
iiig

>>> Find('..gs','called piiig')
not found#one different letter is enough to return none

>>> Find('..g','called piiig much better: xyzg')
iig#match goes from left to right

>>> Find('..gs','called piiig much better: xyzgs')
yzgs#match tries to work with iig but doesn't find the 's' so returns the one that has the entire pattern


#2.2. Special characters:
	#2.2.1. The '\.':
	>>> Find(r'c\.l','c.lled piiig much better: xyzgs')
	c.l
	>>> Find(r'c\.l','cslled piiig much better: xyzgs')
	not found #\. means it must be a dot and not any character
 
	#2.2.2. The '\w':
	>>> Find(r':\w\w\w','blah:cat blah blah')
	:cat

	#2.2.3. The '\d':
	>>> Find(r'\d\d\d','blah:cat bla123h blah')
	123

	#2.2.4 The '\s':
	>>> Find(r'\d\s\d\s\d','blah:cat bla1 2 3h blah')
	1 2 3

	#2.2.5. The '+':
	>>> Find(r'\d\s+\d\s\d','blah:cat bla1     2 3h blah')
	1     2 3
	
	>>> Find(r'\d\s+\d\s\d','blah:cat bla12 3h blah')
	not found
	
	>>> Find(r':\w+','blah blah :kitten blah blah')
	:kitten#gets the first word after :

	#2.2.6. The '\S':
	>>> Find(r':\S+','blah blah :kié&é))=*-/tten blah blah')
	:kié&é))=*-/tten

	>>> Find(r'\w+@\w+','blah hamza.a@gmail.com  blah')
	a@gmail

	>>> Find(r'\S+@\S+','blah hamza.a@gmail.com  blah')
	hamza.a@gmail.com

	>>> Find(r'[\w.]+@[\w.]+','blah hamza.a@gmail.com  blah') #all set of characters before and after @
	hamza.a@gmail.com

	#2.2.7. The () groups:
	>>> m=re.search(r'([\w.]+)@([\w.]+)','blah hamza.a@gmail.com  blah')
	>>> m.group(1)
	'hamza.a'
	>>> m.group(2)
	'gmail.com'


