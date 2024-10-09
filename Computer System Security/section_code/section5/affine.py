

# Encryption using Affine Cipher

def affineEnc(text, k1 ,k2):
  cipher = ''
  for i in text:
    if i == ' ':
      c = ' '
    else:
      if i.isupper():
        c = chr( ((( ord(i) - 65 ) * k1) + k2) % 26 + 65 )
      else:
        c = chr( (((ord(i)- 97 ) * k1) + k2) % 26 + 97 )
    cipher += c
  return cipher

# Decryption using Affine Cipher
def affineDec(text, k1 ,k2):
  plain = ''
  for i in text:
    if i == ' ':
      c = ' '
    else:
      if i.isupper():
        c = chr( (( ord(i) - 65 - k2 ) * k1) % 26 + 65 )
      else:
        c = chr( (( ord(i) - 97  - k2 ) * k1) % 26 + 97 )
    plain += c
  return plain

text = 'Mahmoud Adel Ali Mohamed'
# text = "Hello World"
cipher = affineEnc(text,7,2)
plain = affineDec(cipher,15,2)

print(cipher)
print(plain)
