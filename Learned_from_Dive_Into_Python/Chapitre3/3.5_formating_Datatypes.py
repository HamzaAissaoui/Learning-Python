"""This file contains all commands in chapter 3.5:
	1.1 Introducing String Formatting
	1.2 String Formatting vs. Concatenating

"""


# 1.1 Introducing String Formatting

k = "uid"
v = "sa"
"%s=%s" % (k, v) 	# Output: 'uid=sa'
				 	# Note that (k, v) is a tuple.

# 1.2 String Formatting vs. Concatenating

userCount = 6
print ("Users connected: %d" % (userCount, )) # Note: the comma is necassary in the tuple to be recognized
# Output: Users connected: 6
print "Users connected: " + userCount #Output: Exception can't concatenate string with int.

# 2. Formatting Numbers

print ("Today's stock price: %f" % 50.4625)			#Output: 50.462500  
# %f prints it to six decimal places.
print ("Today's stock price: %.2f" % 50.4625)		#Output: 50.46
# %.2f truncates it to two decimal places. 
print ("Change since yesterday: %+.2f" % 1.5)		#Output: +1.50
# The + modifier displays a '+' or '-' sign before the value.


