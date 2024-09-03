number = input('number')
mapped_numbers = {
    '1' : 'one',
    '2' : 'two', 
   '3' : 'three', 
   '4' : 'four', 
   '5' : 'five', 
}
output = ''
for item in number:
    output += mapped_numbers.get(item, "!!") + " "
print(output)


# more with dictionaries  emoji converter 
message = input('>')
words = message.split(" ")
emojies = {
    ';(':'😉',
    ':)':'😊',
    ':(':'😕'
}
output = ''
for item in words:
    output += emojies.get(item , item) + ' '
print(output)
    
    