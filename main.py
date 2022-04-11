import decrypt
from split_words import wordninja
from decrypt import vigenere_decryption as vdcp
from decrypt import mono_decryption as mdcp
import re

filename = input("Enter ciphertext txt file name including extension .txt:")
f = open(filename, "r")          # ciphertext.text contains the cipher-text, change the text as you use this program
msg = f.read()
msg = ''.join(filter(str.isalpha, msg))
msg = msg.upper()                 # now msg is a string that consists of only upper case letters
second_keyword = input("Enter second keyword:")
ciphertext = vdcp().vigenere_decrypt(msg, second_keyword, len(second_keyword))
key = mdcp().get_key(ciphertext, 50, 5000)
plaintext =  mdcp().cipher_to_plain_with_key(ciphertext, key)
segmented_plaintext = wordninja.split(plaintext)
print("The best key that the program generated is: \n")
print("Plain Alphabet:      ",  "".join(mdcp().alpha))
print("Encryption Alphabet: ",  "".join(key))
print("The segmented plaintext is:")
print(" ".join(segmented_plaintext).lower())