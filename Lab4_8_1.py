import os
import hashlib

"""Count the number of mp3 files"""
count = 0
for (dirname, dirs, files) in os.walk('.'):
   for filename in files:
       if filename.endswith('.mp3') :
           count = count + 1
print ('MP3 Files:', count)


"""Prints out the size"""
for (dirname, dirs, files) in os.walk('.'):
   for filename in files:
       if filename.endswith('.mp3') :
           thefile = os.path.join(dirname,filename)
           print (os.path.getsize(thefile), thefile)


"""Prints out duplicates of mp3 files"""
unique = dict()
for filename in os.listdir('.'):
    if os.path.isfile(filename):
        filehash = hashlib.md5(open(filename, 'rb').read()).hexdigest()

        if filehash not in unique: 
            unique[filehash] = filename
        else:
            print (filename + ' is a duplicate of ' + unique[filehash])
