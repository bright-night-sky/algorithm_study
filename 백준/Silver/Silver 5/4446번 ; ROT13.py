# https://www.acmicpc.net/problem/4446

from sys import stdin


vowels = ('a', 'i', 'y', 'e', 'o', 'u')
consonants = ('b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f')

while True:
    sentence = stdin.readline().rstrip()
    origin_sentence = ''

    for char in sentence:
        origin_char = None
        is_upper = False

        if ord('a') <= ord(char) <= ord('z') or ord('A') <= ord(char) <= ord('Z'):
            if char.isupper():
                char = char.lower()
                is_upper = True

            if char in vowels:
                char_idx = vowels.index(char)
                origin_char = vowels[char_idx - 3]
            elif char in consonants:
                char_idx = vowels.index(char)
                origin_char = vowels[char_idx - 3]

            if is_upper:
                origin_char = origin_char.upper()
        else:
            origin_sentence += char

        origin_sentence += origin_char

    print(origin_sentence)