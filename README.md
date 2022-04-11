# Polyalphabetic Decoder
A program that attempts to decode Polyalphabetic encrypted texts with minimal human supervision.  
This encryption is introduced in “Applied Combinatorics”, Sixth Edition, by A.Tucker, John Wiley & Sons.  
The ciphertext is encrypted in two stages:  
1. Monoalphabetic Substitution based on the first keyword.  
2. Vigenere Cipher based on the second keyword.(In this program, assuming the keyword is either length 4 or 5 for analytical simplicity)  

# How does it work?
User Guide included in the jupyter notebook.

# Requirements
* collections, math, random  
* tabulate  
* six  
* gzip, os, re  

# Citing:
1. Using wordninja to split merged words(This is called word segmentationin NLP). English Model in wordninja is included in this git repo. Source: https://github.com/keredson/wordninja  
2. English trigram frequencies. Source: http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/english-letter-frequencies/  

# Usage
This decryption is the final project for Graph Theory course at Stony Brook.  
However, in the course, it is not required to write a computer program, and this is maybe the first computer program that attempts to decode automatically.

# Alternatives
Alternatives, one can do it without any code. Decryption by hand is feasible but, of course, time consuming; it probably will take around the same amount of time, if not more, to do everything solely by hand as to write this program, but programs are reusable. Once it is coded up, in just a few minutes, it can decrypt all different cipher-texts for all students in the class.  