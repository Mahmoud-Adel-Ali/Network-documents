k1 = 7
k2 = 2
plaintext = "hello world"
result = ''
for c in plaintext:
  if (c != ' '):
    if (c.isupper()):
      # Encrypt uppercase characters
      s = chr((((ord(c) - 65) * k1) + k2) % 26 + 65)
    else:
      # Encrypt lowercase characters
      s = chr((((ord(c) - 97) * k1) + k2) % 26 + 97)
  else:
    s = ' '
  result += s
print(result)