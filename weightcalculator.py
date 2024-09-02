weight = int(input('Enter weight: '))
unit = (input ('(L)bs or (k)g: ')).upper()
if  unit == 'L':
    CON = weight * 0.45
    print(f"youre {CON} kilos")
else:
    CON = weight / 0.45
    print(f"youre {CON} pounds")

    




#this is the use of a for loop 