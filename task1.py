with open("Street_Centrelines.csv") as file:
 
 a = [tuple (line( [STR_NAME],[FULL_NAME],[FROM_STR],[TO_STR] ))for line in file]

print (a)


def histogram (file):
 d = {}
 for row in file:
  key="MAINTENANCE" 
  val="number of streets"
  (key,val) = row
  d[int(key)] = val
 print(d)

def unique(file):
 uni=[]
 x= file_contents.split()
 for word in x:
 	if word not in uni:
 		uni.append(word)  
 		print (uni)


