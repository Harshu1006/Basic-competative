vowels = 'aeiouAEIOU'
s = 'aeiOUz'
s = s + s
result = ""

for i in s:
    if i.isupper():
        continue
    elif i in vowels:
        result += "#"
    else:
        result += i

print(result)
