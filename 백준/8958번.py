# https://www.acmicpc.net/problem/8958

test_case = int(input())

for i in range(0, test_case):
    case = input()
    score = 0
    one_score_stack = 0

    for one_result in case:
        if one_result == 'O':
            score += 1
            score += one_score_stack
            one_score_stack += 1
        else:
            one_score_stack = 0

    print(score)
