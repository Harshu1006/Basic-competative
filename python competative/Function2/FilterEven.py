def fun(a):
    return a % 2 == 0
sequence = [1, 2, 3.5, 4, 6.0, 7, 8]
filtered = list(filter(fun, sequence))
print(filtered)