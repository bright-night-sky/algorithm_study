# https://codeup.kr/problem.php?id=6083

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 빨녹파 각 빛의 가짓수를 공백을 두고 입력합니다.
# 각각 정수형으로 만들고 변수에 넣어줍니다.
r, g, b = map(int, stdin.readline().split(' '))

# r, g, b의 값을 각각 출력할 때, b가 0부터 가장 먼저 증가하고,
# 그 다음은 g, 마지막으로 r의 값이 증가하는 오름차순으로 출력합니다.
# 그래서 r에 대한 값을 가장 바깥 반복문으로, 중간에는 g에 대한 값을 반복문,
# 가장 안쪽에는 b에 대한 값을 반복문으로 처리합니다.
# r의 값을 0부터 r - 1까지 반복합니다.
for r_num in range(r):
    # g의 값을 0부터 g - 1까지 반복합니다.
    for g_num in range(g):
        # b의 값을 0부터 b - 1까지 반복합니다.
        for b_num in range(b):
            # 현재 r, g, b의 값을 공백으로 구분해 출력합니다.
            print(r_num, g_num, b_num)

# r, g, b의 값이 다른 경우의 개수를 출력합니다.
print(r * g * b)