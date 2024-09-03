#created a function using the emoji converter dictionary

def Emoji_maker(message):
    words = message.split(" ")
    emojies = {
    ';(':'😉',
    ':)':'😊',
    ':(':'😕'
    }
    output = ''
    for item in words:
        output += emojies.get(item , item) + ' '
    return output 

message = input('>')
print(Emoji_maker(message))
    
    