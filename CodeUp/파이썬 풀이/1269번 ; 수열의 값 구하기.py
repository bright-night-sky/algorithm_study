# https://codeup.kr/problem.php?id=1269

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 시작 값 a, 곱할 값 b, 더할 값 c, 몇 번째 항인지 나타내는 정수 n을 공백으로 구분해 입력합니다.
# -9 <= a, b, c <= 9
# 1 <= n <= 9
# 각각 int형으로 변환합니다.
a, b, c, n = map(int, stdin.readline().split())

# 첫 번째 항은 시작 값 a이므로 n - 1번 반복 계산하면 n번째 항을 구할 수 있습니다.
# 따라서 n - 1번만큼 반복해봅니다.
for _ in range(n - 1):
    # 현재 항의 값인 a의 값에 b를 곱하고 c를 더해 다시 변수 a에 저장합니다.
    a = a * b + c

# 수열의 n번째 항의 값인 a의 값을 출력합니다.
print(a)