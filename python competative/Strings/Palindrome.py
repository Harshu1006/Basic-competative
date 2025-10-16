k = int(input("Num of Inputs: "))
for i in range(k):
    s = input("Input string: ")
    if s == s[::-1]:
        print(1)
    else:
        print(0)