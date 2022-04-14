import decrypt
from split_words import wordninja
from decrypt import vigenere_decryption as vdcp
from decrypt import mono_decryption as mdcp
import re
import numpy
import itertools


filename = "ciphertext3.txt"    # ciphertext.txt contains the cipher-text, change the text as you use this program
f = open(filename, "r")
msg = f.read()
msg = ''.join(filter(str.isalpha, msg))
msg = msg.upper()                 # now msg is a string that consists of only upper case letters


def get_plaintext():
    second_key_length = vdcp().second_key_word_length(msg)
    freq_strips = vdcp().frequency_strip(msg, second_key_length)
    txt_len = len(msg)
    guess_shifts = vdcp().get_guess_shifts(freq_strips, txt_len, 3)
    freq_dict = mdcp().get_frequency_dictionary()
    best_rating = 0
    for guess_shift in guess_shifts:
        second_keyword = "A"
        for s in guess_shift:
            second_keyword += chr(65+s)
        ciphertext = vdcp().vigenere_decrypt(msg, second_keyword, len(second_keyword))
        sub, rating = mdcp().get_key(ciphertext, 30, 5000, freq_dict)
        if rating > best_rating:
            best_rating = rating
            best_sub = sub
            best_v_keyword = second_keyword
    ciphertext = vdcp().vigenere_decrypt(msg, best_v_keyword, len(best_v_keyword))
    plaintext =  mdcp().cipher_to_plain_with_key(ciphertext, best_sub)
    segmented_plaintext = wordninja.split(plaintext)
    print(" ".join(segmented_plaintext).lower())
    return segmented_plaintext, best_v_keyword, best_sub




if __name__ == "__main__":
    get_plaintext()