'''
Develop a Python program to count the frequency of words and characters in a text string.
'''
text = input("Enter a text string: ")
 
words = text.lower().split()

wfe = {}
for w in words:
    if w in wfe: wfe[w] += 1
    else: wfe[w] = 1
 
cfe = {}
for c in text.lower():
    if c != " ":
        if c in cfe: cfe[c] += 1
        else: cfe[c] = 1

print("\nWord Frequency:")
for w,n in wfe.items():  print(w,":",n)

print("\nCharacter Frequency:")
for c,n in cfe.items():  print(c,":",n)