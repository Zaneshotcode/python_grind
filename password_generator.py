import random 
letters = ['a','b','c','d','e','f','g','h','i','k','l','m','n']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','$','#','%','^','&','*','(',')']

how_many_letters = int(input("how many letters would you like in your passwd? \n"))

how_many_symbols = int(input("how many symbols would you like? \n"))

how_many_numbers = int(input("how many numbers would you like ? \n"))

#easy level 
print("")
# password = ""

# for char in range(0, how_many_letters):
#     password += random.choice(letters)
    
# for char in range(0, how_many_symbols):
#     password += random.choice(symbols)

# for char in range(0, how_many_numbers):
#     password += random.choice(numbers)

# print(password)

#hard level
password_list = []

for char in range(0, how_many_letters):
    password_list.append(random.choice(letters))
    
for char in range(0, how_many_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, how_many_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"your password is : {password}")
    

    