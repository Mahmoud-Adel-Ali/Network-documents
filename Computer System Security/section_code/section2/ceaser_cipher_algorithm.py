
print(chr(65))
print(ord('A'))
s = "welcome"
print(s.isupper())
print(s.islower())
# .....................................
# ceaser cipher algorithm
    # Encreption
text = input("enter text that's you want ancriptio : ")
k=5
result = ''
for i in range (len(text)):
  char = text[i]
  if(char.isupper()):
    # encreption uppercase character
    s = chr(( ord(char) - 65 + k ) % 26 + 65 )
  else:
      s= chr(( ord(char) - 97 + k ) % 26 + 97)
  result += s

print(result)


    # decription
text = result
result=''
for i in range (len(text)):
  char = text[i]
  if(char.isupper()):
    # encreption uppercase character
    s = chr((ord(char)-65-k)%26 + 65)
  else:
      s= chr((ord(char) - 97 - k)% 26 + 97)
  result += s

print(result)


