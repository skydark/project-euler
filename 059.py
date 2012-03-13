#!/usr/bin/python
# -*- coding: utf-8 -*-

#Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

#A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

#For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

#Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

#Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher1.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

#Answer:
	#107359

from time import time; t=time()

K = 3
data = [int(c) for c in open('059-cipher1.txt').read().split(',')]

E = ord(' ')
data_split = [data[i:len(data):K] for i in range(K)]

password = [0]*K
for cnt, chars in enumerate(data_split):
    pool = {}
    for c in chars:
        pool.setdefault(c, 0)
        pool[c] += 1
    password[cnt] = max((v, k) for k, v in pool.items())[1] ^ E



original_text = ''.join(''.join(chr(data_split[i][j]^password[i]) for i in range(K)) for j in range(len(data_split[-1])))+\
''.join(chr(data_split[i][-1]^password[i]) for i in range(len(data) % K))
password = ''.join(chr(c) for c in password)
print(sum(ord(c) for c in original_text))#, password, original_text, time()-t
