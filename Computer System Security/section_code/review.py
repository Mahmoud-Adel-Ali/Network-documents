




def pos(text,k):
  c= ' '
  for i in range(k):
    p = i
    while p < len(text):
      c += text[p]
      p += k
  return c

text = input("enter text : ")

k = int(input("enter key : "))

print(pos(text,k))

