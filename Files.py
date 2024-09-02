f = open('data.txt','w')
#create a new file to wwrite
f.write('hello\n')
#write string
f.write('woorld\n')
f.close()
#close the file and flush output

import os
print(os.getcwd())