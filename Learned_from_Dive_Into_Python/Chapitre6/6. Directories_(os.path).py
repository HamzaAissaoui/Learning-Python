"""Commands to remember:
1. os.path.join("[path]", "[filename]"): joins them and returns and prints it.

2. os.path.expanduser("~"): returns the home directory of the user.

3. os.path.split("[path]\\[file.extention]"): returns a tuple containing the path, the file.

4. os.path.splitext("filename"):returns a tuple containing the filename and the file extension.

5. os.listdir("directory"): returns a list that contains all the files and subdirectories in the path.

6. os.path.isfile("c:\\music\\[file or subdirectory]"): returns boolean, if it's a file returns True, if it's a subdirectory returns False.

7. os.path.isdir("c:\\music\\[file or subdirectory]"): returns boolean, if it's a subdirectory returns True, if it's a file returns False.

8. os.path.normalize(file): normalize the files depending on the operating system.

9. glob.glob('c:\\music\\_singles\\*.mp3'): returns a list of all the mp3 files in singles. (works with all extensions and even directories)

10. glob.glob('c:\\music\\_singles\\s*.mp3'): returns a list of mp3 files that start with s.

11. glob.glob('c:\\music\\*\\*.mp3'): returns all mp3 files in all subdirectories of music and their subdirectories
"""

#1. Constructing Pathnames:
>>> import os.pat
>>> os.path.join("c:\\music\\", "song.mp3")
'c:\\music\\song.mp3'

>>> os.path.join("c:\\music", "song.mp3")
'c:\\music\\song.mp3'	#join adds the \\

>>> os.path.expanduser("~")
'c:\\users\\dell'

>>> os.path.join(os.path.expanduser("~"),"Python")
#construct pathnames for directories and files under the
#user's home directory.
'c:\\users\\dell\\Python'


#2. Splitting Pathnames:
>>> os.path.split("c:\\music\\song.mp3")
('c:\\music', 'song.mp3')#tuple containing path and filename

>>> (filepath, filename) = os.path.split("c:\\music\\song.mp3")
>>> filepath 
'c:\\music'
>>> filename 
'song.mp3'

>>> (shortname, extension) = os.path.splitext(filename)
>>> shortname
'song'
>>> extension
'.mp3'


#3. Listing Directories:
>>> os.listdir("c:\\music\\singles\\")
['a_time_long_forgotten_con.mp3', 'hellraiser.mp3',
'kairo.mp3', 'long_way_home1.mp3', 'sidewinder.mp3',
'spinning.mp3']

>>> dirname = "c:\\"
>>> os.listdir(dirname)
['AUTOEXEC.BAT', 'boot.ini', 'CONFIG.SYS', 'cygwin',
'docbook', 'Documents and Settings', 'Incoming', 'Inetpub', 'IO.SYS',
'MSDOS.SYS', 'Music', 'NTDETECT.COM', 'ntldr', 'pagefile.sys',
'Program Files', 'Python20', 'RECYCLER',
'System Volume Information', 'TEMP', 'WINNT']

>>>	[f for f in os.listdir(dirname) 
		if os.path.isfile(os.path.join(dirname, f))] #returns all the files in dirname.
['AUTOEXEC.BAT', 'boot.ini', 'CONFIG.SYS', 'IO.SYS', 'MSDOS.SYS',
'NTDETECT.COM', 'ntldr', 'pagefile.sys']

>>> [f for f in os.listdir(dirname)
		if os.path.isdir(os.path.join(dirname, f))]	#returns subdirectories in dirname
['cygwin', 'docbook', 'Documents and Settings', 'Incoming',
'Inetpub', 'Music', 'Program Files', 'Python20', 'RECYCLER',
'System Volume Information', 'TEMP', 'WINNT']

#4. Listing Directories in fileinfo.py:

def listDirectory(directory, fileExtList):
	"get list of file info objects for files of particular extensions"
	fileList = [os.path.normcase(f)\#normalize the files depending on the operating system
					for f in os.listdir(directory)]  
					
	fileList = [os.path.join(directory, f)\
					for f in fileList\
						if os.path.splitext(f)[1] in fileExtList] #returns the files who's extensions are in the fileExtlist

#5. Listing Directories with glob:
>>> os.listdir("c:\\music\\singles\\")	#returns all the filenames in the directory
['a_time_long_forgotten_con.mp3', 'hellraiser.mp3',
'kairo.mp3', 'long_way_home1.mp3', 'sidewinder.mp3',
'spinning.mp3']

>>> import glob
>>>	glob.glob('c:\\music\\_singles\\*.mp3')
['c:\\music\\_singles\\a_time_long_forgotten_con.mp3',
'c:\\music\\_singles\\hellraiser.mp3',
'c:\\music\\_singles\\kairo.mp3',
'c:\\music\\_singles\\long_way_home1.mp3',
'c:\\music\\_singles\\sidewinder.mp3',
'c:\\music\\_singles\\spinning.mp3']

>>> glob.glob('c:\\music\\_singles\\s*.mp3')
['c:\\music\\_singles\\sidewinder.mp3',
'c:\\music\\_singles\\spinning.mp3']

>>> glob.glob('c:\\music\\*\\*.mp3')
# returns all mp3 files in all subdirectories of music and their subdirectories