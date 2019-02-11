import os

def sed(pstring,rstring,file1,file2):
	readFile = open(file1)

	writeFile = open(file2,'w+')

	for line in readFile:
		if pstring in line:
			print ("pattern string in line")

			newLine = line.replace(pstring,rstring)
			writeFile.write(newLine)

		else:
			writeFile.write(line)


sed('this','HELLO WORLD','file','outputFile')
