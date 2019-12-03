"""Commands to remember:
1.  try:
		cmds
	finally:
		cmds	#Always execute no matter what happens

2. 	pass: don't do anything just pass.

3. file.('filename').read(): read the entire file.  

		
"""
#1. Handling I/O Errors:
	#File Objects in MP3FileInfo:
	try:
		fsock = open("filename","rb",0)
		try:
			fsock.seek(128,-2)
			tagdata = fsock.read(128)
	
		finally:
			fsock.close()
		.
		.
		.
	except IOError:
		pass

#2. Writing to Files:
"""
	"Append" mode will add data to the end of the file.
	"write" mode will overwrite the file.
"""
#2.1 write mode:
>>> logfile = open('test.log', 'w')
>>> logfile.write('test succeded')
>>> logfile.close()

>>> print file('test.log').read()
test succeeded

#2.2 append mode
>>> logfile = open('test.log', 'a')
>>> logfile.write('line 2')
>>> logfile.close()

>>> print file('test.log').read()
test succeededline 2


	