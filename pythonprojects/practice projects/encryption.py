import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key :{key}")

#ENCRYPT
plaintext = input("Enter a message to encrypt: ")
ciphertext = ""

for letter in plaintext:
    index = chars.index(letter)
    ciphertext += key[index]

print(f"original message: {plaintext}")
print(f"encrypted message: {ciphertext}")


#DECRYPT
ciphertext = input("Enter a message to decrypt: ")
plaintext = ""

for letter in ciphertext:
    index = key.index(letter)
    plaintext += chars[index]

print(f"encrypted message: {ciphertext}")
print(f"original message: {plaintext}")