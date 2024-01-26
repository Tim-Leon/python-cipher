import random;
import math;
key = "fcpevqkzgmtrayonujdlwhbxsi"
text = "On a dark desert highway Cool wind in my hair"
def encrypt(text:str, key:str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for letter in text:
        if letter.lower() in alphabet:
            result += key[alphabet.find(letter.lower())]
        else:
            result += letter
    return result

def decrypt(text:str, key:str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for letter in text:
        if letter.lower() in key:
            result += alphabet[key.find(letter.lower())]
        else:
            result += letter
    return result

encrypted_result = encrypt(text,key)
print(encrypted_result)
print(decrypt(encrypted_result,key))

def split_len(seq, length):
   return [seq[i:i + length] for i in range(0, len(seq), length)]
def encode_transposition(key:str, plaintext:str):
    order = { int(ord(val)): num for num, val in enumerate(key) }
    ciphertext = ''
    sort = sorted(order.keys()) 
    for index in sorted(order.keys()):
       for part in split_len(plaintext, len(key)):
            try:
              ciphertext += part[order[index]]
            except IndexError:
                continue   
    return ciphertext

def decode_transposition(key:str, plaintext:str):
    order = { int(ord(val)): num for num, val in enumerate(key) }
    ciphertext = ''
    for index in sorted(order.keys()):
       for part in split_len(plaintext, len(key)):
            try:
              ciphertext += part[order[index]]
            except IndexError:
                continue   
    return ciphertext
# Encryption
def columnar_encrypt(text, key):
    m = { i : [] for i in key }
    cols = [list(text[j:j+len(key)]) for j in range(0, len(text), len(key))]
    if len(cols[-1]) < len(key):
        while len(cols[-1]) != len(key):
            cols[-1].append(' ')
    i = 0
    for k in m.keys():
        if i < len(key):
            for j in cols:
                m[k] += j[i]
            i += 1
    s = {k : m[k] for k in sorted(m)}
    cipher = ''
    for i in s.keys():
        for x in s[i]:
            cipher += x
    print(m)
    return cipher
def columnar_decrypt(cipher, key):
    if len(cipher) < len(key):
        key = key[:len(cipher)]
    n = len(cipher) // len(key)
    s = { k : [] for k in sorted(key) }
    cols = [cipher[j:j+n] for j in range(0, len(cipher), n)]    
    i = 0
    for k in s.keys():
        if i < len(key):
            s[k] = list(cols[i])
            i += 1
    m = {}  
    for k in key:
        m[k] = s[k]
    o = m
    plain = ''
    import pandas as pd
    m = pd.DataFrame(m)
    for i in m.itertuples():
        for j in i[1:]:
            plain += j
    print(s, '\n')
    return plain.strip()
print(text)
trans = columnar_encrypt("hello",key)
def columnar_encrypt():
    plain = input("Enter the plain text: ").replace(' ', '')
    key = list(input("Enter the plain key: ").lower())
    rowSize = len((key))
    m = [(list(plain[i: i + rowSize])) for i in range(0, len(plain), rowSize)]
    for i in m:
        if len(i) != rowSize:
            while len(i) != rowSize:
                i.append('')
        print(i)
    key_sort = []
    for i in sorted(key):
        key_sort.append(key.index(i))
        key[key.index(i)] = ''
    print(key_sort)
    cipher = []
    for i in key_sort:
        for j in range(len(m)):
            if m[j][i] is not '':   
                cipher.append(m[j][i])
    return 'Cipher Text: Read if you can: {0}'.format(''.join(cipher))
columnar_encrypt()
print(trans)

print(columnar_decrypt(trans))


# Function for nth Fibonacci number
def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(10))