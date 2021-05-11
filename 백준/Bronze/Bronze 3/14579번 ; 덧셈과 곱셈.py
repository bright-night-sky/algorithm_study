# https://www.acmicpc.net/problem/14579

# 첫째 줄에 a, b를 입력합니다.
# 1 <= a < b <= 1000
a, b = map(int, input().split(' '))

# 1부터 n까지 더하는 함수를 만듭니다.
def n_sum(n):
    return int(n * (n+1) / 2)

# 결과를 저장하는 변수입니다.
result = 1

# 문제에서 주어진 식을 그대로 구현합니다.
for i in range(a, b+1):
    result *= n_sum(i)

# 모두 곱한 결과에 14579로 나눈 나머지를 결과 변수 저장합니다.
result %= 14579

# 결과를 출력합니다.
print(result)