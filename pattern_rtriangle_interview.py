#2 spaces
def pyramid(rows):
	for x in range(rows):
		print('  '*(rows-x-1)+'*'*(2*x+1))

pyramid(4)


"""
output
-------
      *
    ***
  *****
*******

"""
