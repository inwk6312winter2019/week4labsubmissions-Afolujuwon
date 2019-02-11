import os
l=[]

def listing(dirname):
	for name in os.listdir(dirname):
		l.append(name)

	print(l[::-1])


listing("/")
