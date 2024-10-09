 # Encryption using Transposition Cipher

def transpositionEnd(text,key):
  cipher = [''] * key
  for column in range(key):
    pointer = column

    while pointer < len(text):
      cipher[column] += text[pointer]
      pointer += key
  return ''.join(cipher)

text = "Mahmoud Adel Ali"

cipher = transpositionEnd(text , 4)

print(cipher)
print(transpositionEnd(cipher , 4))