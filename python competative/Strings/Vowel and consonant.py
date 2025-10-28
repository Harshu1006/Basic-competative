T = int(input("Num of inputs: "))

for _ in range(T):
    s = input("Input string: ")
    vowel_count = 0
    consonant_count = 0
    for i in s:
        if i isalpha():
                if i in "aeiouAEIOU":
            vowel_count+=1
        else:
            consonant_count+=1

    print(f"vowels: {vowel_count} consonants: {consonant_count}")
