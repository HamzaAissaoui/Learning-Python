
def info(object, spacing=10, collapse=1):
	"""Print methods and doc strings.

	Takes module, class, list, dictionary, or string."""

	methodList = [method for method in dir(object) if callable(getattr(object, method))]

	processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
	
	print ("\n".join(["%s %s" %	(method.ljust(spacing), \
			
			processFunc(str(getattr(object, method).__doc__))) \
			
			for method in methodList]))

if __name__ == "__main__":
	print (info.__doc__)


#What this function does:
li = []
info(li)
'''
append 		L.append(object) -- append object to end
count 		L.count(value) -> integer -- return number of occurrences of value
extend 		L.extend(list) -- extend list by appending list elements
index 		L.index(value) -> integer -- return index of first occurrence of value
insert 		L.insert(index, object) -- insert object before index
pop 		L.pop([index]) -> item -- remove and return item at index (default last)
remove 		L.remove(value) -- remove first occurrence of value
reverse 	L.reverse() -- reverse *IN PLACE*
sort 		L.sort([cmpfunc]) -- sort *IN PLACE*; if given, cmpfunc(x, y) -> -1, 0, 1
'''