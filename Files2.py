f = open('data.txt')
text = f.read()
print (text)
#this changes the vcontent of the file from what it was before
f2 = open ('data.txt','a+')
f2.write('howre you \n')
userinput = input() + '\n'
f2.close()
#this updates whats in the file and just prints it uut 
f2 = open('data.txt')
text = f2.read()
print (text)