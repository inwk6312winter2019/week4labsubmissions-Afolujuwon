from string import punctuation, whitespace

fil = open('file','r')

file = fil.read().split()
#with open(file, 'r') as fd:
#	words = fd.read().split()


def counter():
	word_counter = {}
	for word in file: 
		if len(word) > 0 and word != '\r\n':
			if word not in word_counter: 
				word_counter[word] = 1
			else:
				word_counter[word] += 1 

	for i,word in enumerate(sorted(word_counter,key=word_counter.get,reverse=True)[:20]):
    
		print(i+1,word,word_counter[word])


counter()
