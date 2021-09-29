# https://codeup.kr/problem.php?id=1297

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 길이 n을 입력합니다.
# int형으로 변환합니다.
n = int(stdin.readline())
# 단면의 넓이 S의 최댓값을 저장할 변수를 선언합니다.
# 0으로 초기화합니다.
max_s = 0
# 단면의 넓이 S가 최댓값일 때, 양 끝에서 구부린 길이를 저장할 변수를 선언합니다.
# 1로 초기화합니다.
max_s_bend_len = 1

# 구부린 길이를 1부터 n // 2 - 1까지 반복해봅니다.
for bend_len in range(1, n // 2):
    # 현재 구부린 길이에서 단면의 넓이 S를 계산해봅니다.
    s = bend_len * (n - 2 * bend_len)

    # 현재 구부린 길이에서 단면의 넓이 S가 이전까지의 단면의 최대 넓이보다 크다면
    if s > max_s:
        # max_s에 현재 단면의 넓이 S를 저장합니다.
        max_s = s
        # max_s_bend_len에 현재 구부린 길이를 저장합니다.
        max_s_bend_len = bend_len

# 단면의 넓이 S가 최대일 때 구부린 길이를 저장하고 있는 max_s_bend_len의 값을 출력합니다.
print(max_s_bend_len)