# https://www.acmicpc.net/problem/4659

while True:
    password = input()

    if password == "end":
        break
    else:
        vowels = ['a', 'e', 'i', 'o', 'u']

        vowel_count = 0

        for vowel in vowels:
            vowel_count += password.count(vowel)

