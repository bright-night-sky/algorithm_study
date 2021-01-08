# https://www.acmicpc.net/problem/1075

# 두 정수 N, F 입력
# 100 <= N <= 2000000000 자연수
# 1 <= F <= 100 자연수
N = input()
F = int(input())

# N의 가장 뒤 두자리를 00으로 만들고 숫자 자료형으로 만든다.
num = int(N.replace(N[-2:], '00'))

# 그 숫자를 1씩 증가시켜 보면서 F로 나누어지는지 확인한다.
# 맨 뒤의 두 자리를 변경하는 것이므로 0부터 99까지 더해본다.
for i in range(0, 100):
    if (num + i) % F:
        N = int(N) + i

print(str(N)[-2:])
