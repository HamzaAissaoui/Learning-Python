"""commands to remember:
1. sys.modules.key(): returns all names of modules that have been imported since the start of python.
2. sys.version: returns version of python you're using.
3. sys.modules[key]: returns the module of the key.
4. MP3FileInfo.__module__: returns the wrapper module of the MP3FileInfo class
"""

# Introducing sys.modules:

>>> import sys
>>> print "\n".join(sys.modules.key())
win32api
os.path
os
exceptions
__main__
ntpath
...

# Using sys.modules:

>>> import fileinfo

>>> f
<module 'fileinfo' from 'fileinfo.pyc'>

>>> sys.modules["fileinfo"]
<module 'fileinfo' from 'fileinfo.pyc'>

# The __module__ Class Attribute

>>> from fileinfo import MP3FileInfo

>>> MP3FileInfo.__module__
'fileinfo'

>>> sys.modules[MP3FileInfo.__module__]
<module 'fileinfo' from 'fileinfo.pyc'>

