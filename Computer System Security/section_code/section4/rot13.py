# a b c d e f g h i j k l m
# n o p q r s t u v w x y z

def rot13Encription (string , key):
  cipher = ''
  for i in string:
    if i != '':
      if i.isupper():
        c = ((ord(i) - 65 + key )%26) + 65
      else:
        c = ((ord(i) - 97 + key )%26) + 97
    else: 
      cipher += ''
    cipher += chr(c)
  return cipher

def rot13Decription (string , key):
  plain = ''
  for i in string:
    if i != '':
      if i.isupper():
        c = ((ord(i) - 65 + key )%26) + 65
      else:
        c = ((ord(i) - 97 + key )%26) + 97
    else: 
      plain += ''
    plain += chr(c)
  return plain
print(  rot13Encription("Mahmoud" , 13))
print(  rot13Decription("Znuzbhq" , 13))

