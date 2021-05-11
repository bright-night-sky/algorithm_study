# https://www.acmicpc.net/problem/2355

# 첫째 줄에 두 정수 A, B 입력
# A, B는 정수이다!!!
A, B = map(int, input().split(' '))

if A >= 0 and B >= 0:
    one_to_B = B * (B + 1) / 2
    one_to_A = A * (A + 1) / 2

    if A < B:
        print(one_to_B - one_to_A + A)
    else:
        print(one_to_A - one_to_B + B)
elif A < 0 and B < 0:
    A = -A
    B = -B
    one_to_B = B * (B + 1) / 2
    one_to_A = A * (A + 1) / 2

    if A < B:
        print(-(one_to_B - one_to_A + A))
    else:
        print(-(one_to_A - one_to_B + B))
else:
    pass
