nums = [1, 2, 3, 4, 5, 6]
squares = list(map(lambda x: x * x, nums))
filtered = list(filter(lambda x: x % 3 == 0, squares))
print(filtered)