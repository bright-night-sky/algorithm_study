# https://www.acmicpc.net/problem/16674

# 첫 번째 줄에 양의 정수 N을 입력합니다.
# 1 <= N <= 1,000,000,000
# N은 0으로 시작하지 않습니다.
N = input()

count_2 = N.count('2')
count_0 = N.count('0')
count_1 = N.count('1')
count_8 = N.count('8')

if count_2 + count_0 + count_1 + count_8 == len(N):
    print(1)
elif count_2 >= 1 and count_0 >= 1 and count_0 >= 1 and count_8 >= 1:
    print(2)
elif count_2 == count_0 == count_1 == count_8:
    print(8)
else:
    print(0)