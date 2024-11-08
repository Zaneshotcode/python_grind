# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verrified": True
# }
# customer[""]
# print(customer.get("name"))

# phone = input("phone: ")
# numbers = {
#     "1" : "one",
#     "2" : "two",
#     "3" : "three",
#     "4" : "four"

# }
# output = ""
# for ch in phone:
#     output += numbers.get(ch, "!") + " "
# print(output)

message = input(">")
words = message.split(' ')
emojis = {
    ":)" : "😀",
    ":(" : "🥹"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)