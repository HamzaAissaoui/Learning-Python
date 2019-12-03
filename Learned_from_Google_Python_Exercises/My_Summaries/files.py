"""This will contain all necessary commands for files in python"""

import sys											#necessary module

def Cat(filename):									#function for going through the file
  f = open(filename, 'rU') 							#open in reading mode, U is for normalazing
  for line in f:													
    print line,									#printing each line(the ',' is to get rid of extra line jumps)			
  #or
  #lines=f.readlines()								#returns a list that elements are separated by /n	
  #print lines
  #or 
  #text=f.read()										#returns one big string containing all the text
  #print text,		
  f.close()

def main():
  Cat(sys.argv[1])

if __name__ == '__main__':
  main()