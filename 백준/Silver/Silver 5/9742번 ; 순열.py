# https://www.acmicpc.net/problem/9742

from sys import stdin
from itertools import permutations

while True:
    try:
        test_case = stdin.readline().rstrip().split(' ')

        string = test_case[0]
        position = int(test_case[1])

        string_permutations = list(permutations(string))
        string_permutations_len = len(string_permutations)

        if (position - 1) > string_permutations_len:
            print(f"{string} {position} = No permutation")
        else:
            position_string = string_permutations[position - 1]
            print(f"{string} {position} = {''.join(position_string)}")
    except:
        break
