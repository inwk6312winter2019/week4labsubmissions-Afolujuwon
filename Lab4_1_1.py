#task 1 and task 2

from string import punctuation, whitespace

file = 'file'

with open(file, 'r') as fd:
	words = fd.read().split()


#removes punctuation, whitespaces and uppercase

def readfile(words):
	processed = ''
	for item in words:
		if ((item in punctuation) or (item in whitespace)):
			pass
		else:
			processed += item.lower()
	print (processed)

readfile('file')

print ("{} has {} 'words'".format(file, len([readfile(word) for word in words])))

