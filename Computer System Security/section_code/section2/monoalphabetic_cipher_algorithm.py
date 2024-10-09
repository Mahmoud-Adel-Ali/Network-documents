letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
           's','t','u','v','w','x','y','z']
key = ['q','w','e','r','t','y','u','i','o','p','a','s','d','m','g','h','j','k',
           'l','z','x','c','v','b','n','f']
text = str(input("enter yor text :   ")).lower()
cipher = ''
# encription
for i in text:
  keyNum = letters.index(i)
  newLett  = key[keyNum]
  cipher += newLett
print(cipher)

# 
# decription
text =''
for i in cipher:
  keyNum = key.index(i)
  newLett  = letters[keyNum]
  text += newLett
print(text)
