"""Commands to remember:
1. open("/file", [mode]): opening file in a certain mode.
2. try:
		cmds 			#try to execute these commands
	except [exception]:	
		cmds			#If the exception occurs, do this instead
	else:
		cmds			#If the exceptions don't happen, continue and do this.

3.  try:
		cmds
	finally:
		cmds	#Always execute no matter what happens

"""

#1. opening a non-existent file:
>>> fsock= open("/notthere", "r")
IOError: [Errno 2] No such file or directory: '/notthere'

>>> try: 
		fsock= open(/notthere)
	except IOError:
		print ("the file doesn't exist")
		
	print("this text will always show")

#2. Using Exceptions For Other Purposes:
	#a wrapper module for getting a password from the user. Getting a
	#password is accomplished differently on UNIX, Windows, and Mac OS platforms, but this code encapsulates
	#all of those differences.
	try: 
		import termios, TERMIOS
	except: ImportError:
		try: 
			import msvcrt
		except ImportError: 
			try: 
				from EasyDialogs import AskPassword
			except ImportError:
				getpass = default_getpass
			else:
				getpass = AskPassword
		else:
			getpass = win_getpass
	else:
		getpass = unix_getpass


