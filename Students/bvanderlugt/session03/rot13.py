#!/usr/bin/python

import string

def rot13(text)
    alphabet = string.ascii_lowercase
    for i in alphabet:        
        position = alphabet.index(i)
        letterAtPosition = alphabet[alphabet.index(i)]       
        if position < 13:
            letterAtPosition = alphabet[alphabet.index(i)+13]
        else:
            leftover = 13 - len(alphabet)
            letterAtPosition = alphabet[alphabet.index(i) + leftover]
    return text

rot13("abcd")