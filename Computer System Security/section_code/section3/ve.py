import math

def generateKey(string,key):
  while len(string) > len(key):
    key = key + key
  key = key[:len(string)]
  return key

# this  function return the encryption text
def cipherText(string,key):
  cipher_text = []
  for i in range(len(string)):
    x = (ord(string[i])+ord(key[i])) % 26
    x += ord('A')
    cipher_text.append(chr(x))
  return ("".join(cipher_text))

def originalText(cipher_text , key):
  orig_text = []
  for i in range(len(cipher_text)):
    x = (ord(cipher_text[i])-ord(key[i]) + 26 ) % 26
    x += ord('A')
    orig_text.append(chr(x))
  return ("".join(cipher_text))

string = "MAHMOUD"
k = "HELLO"
key = generateKey(string , k)

cipher_text  =cipherText(string, key)
print("cipher text of ",string , "is ",cipher_text )

print("original text of ",cipher_text , "is ", originalText(string, key))