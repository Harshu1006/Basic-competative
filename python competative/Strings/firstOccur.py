a = 'aabbcc'
B = 98
char = chr(B)
if char in a:
    print(a.index(char))
else:
    print("Not found")