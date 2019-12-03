"""This will contain all necessary commands for dictionnaries in python"""

d={}									#creating a dict

d['hamza']='aissaoui'					#creating an item

d['hamza']								#getting a value from key

d.get('hamza')							#same as above

'hamza'in d 							#testing if value in d

d.keys()								#returns list of keys
 
d.values()								#returns list of values

d.items()								#returns list of tuples containing (key,value) pairs 

for k,v in d.items(): 
	print 'keys:', k, '->', v 			