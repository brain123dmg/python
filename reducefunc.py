from functools import reduce
#m = [1,2,3,4,5,6,7,8,9]
num = []
for i in range(0,8):
    m =int(input())
    num.append(m)
print(num)
print(reduce(lambda x,y : x+y, num))

#p = reduce (lambda x,y: x+y , m)
#print(p)
