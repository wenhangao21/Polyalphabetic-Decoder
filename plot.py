import matplotlib.pyplot as plt
import decrypt
from split_words import wordninja
from decrypt import vigenere_decryption as vdcp
from decrypt import mono_decryption as mdcp
import re
import numpy
import itertools
import matplotlib.gridspec as gridspec

filename = "ciphertext.txt"
f = open(filename, "r")          # ciphertext.text contains the cipher-text, change the text as you use this program
msg = f.read()
msg = ''.join(filter(str.isalpha, msg))
msg = msg.upper()                 # now msg is a string that consists of only upper case letters

second_key_length = vdcp().second_key_word_length(msg)
freq_strips = vdcp().frequency_strip(msg, second_key_length)
freq1 = freq_strips[0]

plt.figure(figsize=(8,3))
plt.bar(vdcp().alpha, height=freq1)
plt.xticks(vdcp().alpha, vdcp().alpha)
axes = plt.gca()
axes.get_yaxis().set_visible(False)
axes.set_ylim([0, 15])
plt.show()