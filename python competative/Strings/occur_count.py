A = 'aboboboboc'
B = 'bob'
count = 0
for i in range(len(A)):
    if A[i:i+3] == B:
        count += 1
print(count)