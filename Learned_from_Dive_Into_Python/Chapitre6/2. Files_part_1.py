"""Commands to remember:
1. open("/file", [mode]): opening file in a certain mode.
2. file.mode: returns the opening mode of file.
3. file.name: returns the directory and name of file.
4. file.tell(): returns the current position in the file ( in bytes)
5. file.seek([number of positions to move],[mode of seeking])
	5.1 seeking mode;
		0: move to a position starting from the begining of the file (position 0)
		1: move from current position.
		2: move to a position related to the end of file so seek(-128,2) means start from the end and go back 128 bytes

6. file.read(128): read the next 128 bytes of the file from whichever position we're in.
7. usually the last 128 bytes of the file contain the tag data.
8. File.close(): closes the file.
9. File.closed: checks if the file is closed (returns boolean)
10.  
"""
#1. Opening a File:

>>> f = open("/music/file.mp3", "rb") #reading and binary

>>> f
<open file '/music/_singles/kairo.mp3', mode 'rb' at 010E3988>

>>> f.mode
'rb'

>>> f.name
'/music/file.mp3'

#2. Reading a file:

>>> f.tell()
0

>>> f.seek(-128, 2)
>>> f.tell()
7542909

>>> tagData = f.read(128)

>>> tagData #usually the last 128 bytes of the file contain the tag data
'TAGKAIRO****THE BEST GOA ***DJ MARY-JANE***
Rave Mix 2000http://mp3.com/DJMARYJANE \037'


#3. Closing Files: It's important to close files as soon as you're finished with them.

>>> f
<open file '/music/_singles/kairo.mp3', mode 'rb' at 010E3988>

>>> f.closed
False

>>> f.close() ❷

>>> f
<closed file '/music/_singles/kairo.mp3', mode 'rb' at 010E3988>

#4. 