alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def caeser(original_text, shift_amount, direction):
    cipher_encrypt = ""
    cipher_decrypt = ""
    if direction == "encode":
        for letter in original_text:
            shifted_amount = alphabet.index(letter) + shift_amount
            shifted_amount %= len(alphabet)
            cipher_encrypt += alphabet[shifted_amount]
        print(f'Here is Encoded result: {cipher_encrypt}')
    elif direction == "decode":
        for letter in original_text:
            shifted_amount = alphabet.index(letter) - shift_amount
            shifted_amount %= len(alphabet)
            cipher_decrypt += alphabet[shifted_amount]
        print(f"Here is Decoded result: {cipher_decrypt}")
caeser(original_text= text, shift_amount= shift, direction = direction)