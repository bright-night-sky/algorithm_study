# https://codeup.kr/problem.php?id=1282

# readline을 사용하기 위해 import합니다.
from sys import stdin


# n을 입력합니다.
# 0 < n <= 2^31
# int형으로 변환합니다.
n = int(stdin.readline())
# n의 제곱근을 구하고 변수에 저장합니다.
root_n = n ** 0.5
# n의 제곱근인 root_n의 값을 int형으로 변환해서 root_n보다 작은 수 중 가장 큰 자연수를 구해 변수에 저장합니다.
t = int(root_n)
# t의 제곱수를 구해 변수에 저장합니다.
n_square = t ** 2
# n에서 t의 제곱수인 n_square를 빼서 k를 구해 변수에 저장합니다.
# 0 < k < n <= 2^31
k = n - n_square

# k, t를 공백으로 구분해 출력합니다.
print(k, t)