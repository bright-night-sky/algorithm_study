# https://codeup.kr/problem.php?id=1288

# readline을 사용하기 위해 import합니다.
from sys import stdin


# n, r을 공백으로 구분해 입력합니다.
# 1 <= r <= n <= 12
# 각각 int형으로 변환합니다.
n, r = map(int, stdin.readline().split())
# n - r을 구해 변수에 저장합니다.
n_minus_r = n - r
# nCr을 계산한 결과를 저장할 변수를 선언합니다.
# 1로 초기화합니다.
ncr = 1

# nCr의 분자 부분을 계산합니다.
# 2부터 n까지 반복해봅니다.
for num in range(2, n + 1):
    # ncr 변수의 값에 현재 숫자를 곱합니다.
    ncr *= num

# nCr의 분모 부분을 계산합니다.
# 2부터 n-r까지 반복해봅니다.
for num in range(2, n_minus_r + 1):
    # ncr 변수의 값에 현재 숫자를 나눠줍니다.
    ncr //= num

# 2부터 r까지 반복해봅니다.
for num in range(2, r + 1):
    # ncr 변수의 값에 현재 숫자를 나눠줍니다.
    ncr //= num

# nCr 결과인 ncr 변수의 값을 출력합니다.
print(ncr)