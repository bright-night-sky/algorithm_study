# https://codeup.kr/problem.php?id=1258

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 자연수 n을 입력합니다.
# int형으로 변환합니다.
n = int(stdin.readline())
# 1부터 n까지의 합을 저장할 변수를 선언합니다.
# 0으로 초기화합니다.
n_sum = 0

# 1부터 n까지 반복해봅니다.
for num in range(1, n + 1):
    # 현재 숫자를 n_sum에 더해줍니다.
    n_sum += num

# 1부터 n까지의 합인 n_sum의 값을 출력합니다.
print(n_sum)