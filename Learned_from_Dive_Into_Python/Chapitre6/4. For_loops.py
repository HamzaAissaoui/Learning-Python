"""Commands to remember:
1. print "\n".join(li): joins the list with \n as a separator.

for k,v in os.environ.items():
		print "%s=%s" % (k, v)	#mapping a dictionary into a list
		
3. print "\n".join(["%s=%s" % (k,v)
					for k,v in os.environ.items()]) : mapping a dictionary into a list
"""

#1. Introducing the for Loop:
>>> li=['a','b','e']
>>> for s in li:
		print s		# the print skips lines
a
b 
e

>>> print "\n".join(li)	#better implementation
a
b 
e

#2. Simple Counters:
>>> for i in range(5):
		print i
0
1
2
3
4

>>> for i in range(len(li)):#3
		print li[i]
a
b 
e	

#3. Iterating Through a Dictionary:
>>> import os
	
>>> for k,v in os.environ.items():
		print "%s=%s" % (k, v)
		
USERPROFILE=C:\Documents and Settings\mpilgrim
OS=Windows_NT
COMPUTERNAME=MPILGRIM
USERNAME=mpilgrim
	
>>> print "\n".join(["%s=%s" % (k,v)
					for k,v in os.environ.items()])
					
USERPROFILE=C:\Documents and Settings\mpilgrim
OS=Windows_NT
COMPUTERNAME=MPILGRIM
USERNAME=mpilgrim
	
#4. for Loop in MP3FileInfo:
tagDataMap = {"title" : ( 3, 33, stripnulls),
"artist" : ( 33, 63, stripnulls),
"album" : ( 63, 93, stripnulls),
"year" : ( 93, 97, stripnulls),
"comment" : ( 97, 126, stripnulls),
"genre" : (127, 128, ord)}

...
#tagdata contains the data we got from the file
if tagdata[:3] == "TAG":
	for tag, (start, end, parseFunc) in self.tagDataMap.items():
		self[tag] = parseFunc(tagdata[start:end])

		
		
