
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#TODO 1: create a fucntion called 'encrypt()' that takes 'original_text' and 'shift_amount as 2 inputs
#Todo 2: Inside the 'encrypt()' function, shift each letter of the 'original_text forwards in the alphabet by the shift_amount and print the encrypted text.

def encrypt(original_text, shift_amount):
    input_text = ""
    for letter in original_text:
        input_text = original_text[index] + shift_amount
print(input_text)
