# def greet_user(name):
#     print(f'Hi {name}')
#     print("welcome aboard")

# greet_user("John")


#return 

from email import message


# def square(number):
#     return number * number 


# print(square(3))

def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)" : "😀",
        ":(" : "🥹"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input(">")
print(emoji_converter(message))