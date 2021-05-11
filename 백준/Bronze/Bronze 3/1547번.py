# https://www.acmicpc.net/problem/1547

cup = [True, False, False]
M = int(input())
for i in range(0, M):
    cup1, cup2 = map(int, input().split(' '))

    cup[cup1 - 1], cup[cup2 - 1] = cup[cup2 - 1], cup[cup1 - 1]

for idx in range(0, len(cup)):
    if cup[idx] == True:
        print(idx + 1)
        break