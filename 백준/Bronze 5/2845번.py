# https://www.acmicpc.net/problem/2845

people, area = input().split(' ')
result = int(people) * int(area)


expect = list(map(int, input().split(' ')))

for i in expect:
    print(i - result, end=' ')