def square(lister):
    listOne=[]
    for p in lister:
        listOne.append(p**2)
    return listOne
    
r = [2, 3, 5, 9]
V = square(r)
print(V)

w = [2, 3, 4, 5]
w[0] = 3
print(w)

y = {2, 3, 5, 3, 3, 5}
print(y)