'''Initializing and Coding Classes'''
'''Important things to remember from this:
1. f.__class__ : returns the class that f belongs to
2. self.data = {} : is an instance attribute, it's only created with each instance.
3. dict1.update(dict2): copies all items from dict2 and merges them to dict1
4. copy module: can copy arbitrary Python objects.

'''
#1. Initializing the FileInfo Class:

class FileInfo(UserDict): #FileInfo inherits from UserDict
"store file metadata" 
def __init__(self, filename=None): 	#filename default value is none, but we can put whatever we want in it
	UserDict.__init__(self) 		#we must also intialize the parent classe
	self["name"] = filename			#when we create an instance and give it a value, it goes to 'name'
	
#2. Instantiating Classes:

>>> import fileinfo					#importing the module

>>> f = fileinfo.FileInfo("/music/_singles/kairo.mp3")		#creating an instance

>>> f.__class__ 
<class fileinfo.FileInfo at 010EC204>						#the classe is indeed FileInfo

>>> f 
{'name': '/music/_singles/kairo.mp3'}						#the value given when instanciating the class is given to 'name'


#3. Exploring UserDict: A Wrapper Class

	#3.1. Defining the UserDict Class
	
	class UserDict:#Doesn't inherit from any class (base class)
		def __init__(self, dict=None):
			self.data = {}
			if dict is not None: self.update(dict) #copies items from dict and puts them in self.data
	
	#3.2. UserDict Normal Methods
	def clear(self): self.data.clear() 
	
	def copy(self): 
		if self.__class__ is UserDict: 
			return UserDict(self.data)
		import copy 
		return copy.copy(self)

	def keys(self): return self.data.keys() 

	def items(self): return self.data.items()

	def values(self): return self.data.values()
	#we must define all these methods to use them on the userdict class and make them its own.
	
#4. Inheriting Directly from Built-In Datatype dict:

class FileInfo(dict): 		#we inherit directly from dict
	"store file metadata"
	def __init__(self, filename=None):
		self["name"] = filename		#we don't need to initialize the dict because it's not a wrapper class

#5. Special Class methods:

	#5.1. The __getitem__ Special Method:
	def __getitem__(self, key): return self.data[key]

	>>> f = fileinfo.FileInfo("/music/_singles/kairo.mp3")
	>>> f
	{'name':'/music/_singles/kairo.mp3'}
	>>> f.__getitem__("name") #we can use this syntax
	'/music/_singles/kairo.mp3'
	>>> f["name"] 				#or this one
	'/music/_singles/kairo.mp3'

	#5.2. The __setitem__ Special Method
	def __setitem__(self, key, item): self.data[key] = item
	>>> f
	{'name':'/music/_singles/kairo.mp3'}
	>>> f.__setitem__("genre", 31) #we can use this one
	>>> f
	{'name':'/music/_singles/kairo.mp3', 'genre':31}
	>>> f["genre"] = 32 #or this one
	>>> f
	{'name':'/music/_singles/kairo.mp3', 'genre':32}

#6. Overriding __setitem__ in MP3FileInfo:

def __setitem__(self, key, item): 
	if key == "name" and item: 
		self.__parse(item) #we do extra parsing of the item when key=name
	FileInfo.__setitem__(self, key, item) #we must call the ancestor method
	
#6.2. Example 5.15. Setting an MP3FileInfo's name
>>> import fileinfo

>>> mp3file = fileinfo.MP3FileInfo() #an MP3Fileinfo instance
>>> mp3file["name"] = "/music/_singles/kairo.mp3" #here we're using the setitem defined above

>>> mp3file
{'album': 'Rave Mix', 'artist': '***DJ MARY-JANE***', 'genre': 31,
'title': 'KAIRO****THE BEST GOA', 'name': '/music/_singles/kairo.mp3',
'year': '2000', 'comment': 'http://mp3.com/DJMARYJANE'}#the extra processing happened

#7. Introducing Class Attributes:

class MP3FileInfo(FileInfo):
	"store ID3v1.0 MP3 tags"
	tagDataMap = {		"title" : ( 3, 33, stripnulls),
'''class attribute'''	"artist" : ( 33, 63, stripnulls),
						"album" : ( 63, 93, stripnulls),
						"year" : ( 93, 97, stripnulls),
						"comment" : ( 97, 126, stripnulls),
						"genre" : (127, 128, ord)}

>>> import fileinfo

>>> fileinfo.MP3FileInfo.tagDataMap #it doesn't need an instance to exist
{'title': (3, 33, <function stripnulls at 0260C8D4>),
'genre': (127, 128, <built-in function ord>),
'artist': (33, 63, <function stripnulls at 0260C8D4>),
'year': (93, 97, <function stripnulls at 0260C8D4>),
'comment': (97, 126, <function stripnulls at 0260C8D4>),
'album': (63, 93, <function stripnulls at 0260C8D4>)}

>>> m = fileinfo.MP3FileInfo() 
>>> m.tagDataMap
{'title': (3, 33, <function stripnulls at 0260C8D4>),
'genre': (127, 128, <built-in function ord>),
'artist': (33, 63, <function stripnulls at 0260C8D4>),
'year': (93, 97, <function stripnulls at 0260C8D4>),
'comment': (97, 126, <function stripnulls at 0260C8D4>),
'album': (63, 93, <function stripnulls at 0260C8D4>)}


