# https://www.acmicpc.net/problem/4659

from sys import stdin

vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    test_case = stdin.readline().rstrip()

    if test_case == "end":
        break
    else:
        is_vowel_in = False
        is_