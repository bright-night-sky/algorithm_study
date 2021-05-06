# https://www.acmicpc.net/problem/2417

# 올림 함수인 ceil을 쓰기 위해 import 합니다.
from math import ceil

# 첫째 줄에 정수 n을 입력합니다.
# 0 <= n < 2^63
n = int(input())

# q^2 >= n인 가장 작은 음이 아닌 정수 q를 저장하는 변수를 선언합니다.
q = ceil(n ** 0.5)

# q를 출력합니다.
print(q)