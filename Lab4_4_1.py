word_file = 'file'
books = [origin, huck, don, great, meta, sherlock, divine, journey]

def words(book):
    list_ = []
    flag = False
    signal = "*** START OF"
    for line in book:
        if flag == True:
            for word in line.split():
                list_.append(word)
        elif (signal in line) and (flag == False):
            flag = True
        else:
            pass
    return list_
    
def clean(word):
    result = ''
    for char in word:
        if (char in whitespace) or (char in punctuation):
            pass
        elif not char.isalpha():
            pass
        else:
            result += char.lower()
    return result

def stats():
    for book in books:
        book_words = set([clean(word) for word in words(open(book, 'r'))])
        words_ = set([word for word in open(word_file, 'r')])
        print("Stats for %s" % open(book, 'r').name
	print("There are", len(book_words - words_))

stats()

print ("\n\nThe words not in the word list for origin.txt:")
print set([clean(word) for word in words(open(origin, 'r'))]) - \
set([word for word in open(word_file, 'r')])
