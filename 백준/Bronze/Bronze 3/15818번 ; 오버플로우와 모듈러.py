# https://www.acmicpc.net/problem/15818

# 첫 줄에 연산될 정수의 개수 N, M을 입력합니다.
# 1 <= N <= 100
# 1 <= M <= 2,147,483,647
N, M = map(int, input().split(' '))

# 두 번째 줄에는 N개의 정수 ai를 한 줄로 입력합니다.
ai = list(map(int, input().split(' ')))

# 결과를 저장할 변수입니다.
# 곱해나가는 결과를 저장하므로 1로 초기화를 해줍니다.
result = 1

# 문제에 나와있는 공식에서 ((A % M) x (B % M))을 구합니다.
for a in ai:
    result *= a % M

# 문제에 나와있는 공식의 마지막 부분인 % M을 계산합니다.
result %= M

# 결과를 출력합니다.
print(result)