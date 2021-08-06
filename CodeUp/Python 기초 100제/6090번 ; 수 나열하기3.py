# https://codeup.kr/problem.php?id=6090

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 시작 값 a, 곱할 값 m, 더할 값 d, 몇 번째 인지를 나타내는 정수 n을 공백을 두고 입력합니다.
# 각각 정수형으로 변환합니다.
a, m, d, n = map(int, stdin.readline().split())
# n번 반복하면서 계산한 현재 수를 저장할 변수를 선언합니다.
# 시작 값이 a이므로 a로 초기화합니다.
cur_num = a

# n번째 수를 구하기 위해 n-1번만큼 반복합니다.
for _ in range(n - 1):
    # cur_num의 값에 m을 곱하고 d를 더한 뒤 다시 cur_num에 넣어줍니다.
    cur_num = cur_num * m + d

# 반복문이 끝나고 n번째 수인 cur_num의 값을 출력합니다.
print(cur_num)