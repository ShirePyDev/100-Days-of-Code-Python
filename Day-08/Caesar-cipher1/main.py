alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

def encrypt(original_text, shift_amount):
    Ceaser = ""
    for letter in original_text:
        shift_Position = (alphabet.index(letter) + shift_amount) % 26
        # shift_Position = shift_Position.len([alphabet]) % 26
        Ceaser += alphabet[shift_Position]
    print(Ceaser)
encrypt(original_text= text, shift_amount= shift)