alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO 1: create a fucntion called 'encrypt()' that takes 'original_text' and 'shift_amount as 2 inputs
#Todo 2: Inside the 'encrypt()' function, shift each letter of the 'original_text forwards in the alphabet by the shift_amount and print the encrypted text.

# hello -> 2
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        cipher_text += alphabet[shifted_position]
    print(f"here is the encoded result: {cipher_text} ")

#todo 4: what happens if you try to shift z forwards by 9? can you fix the code?

#todo3: call the 'encrypt()' function and pass in the user input. Your should



encrypt(original_text=text, shift_amount=shift)