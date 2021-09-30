# https://codeup.kr/problem.php?id=1355

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 역삼각형의 길이를 입력합니다.
# int형으로 변환합니다.
n = int(stdin.readline())

# 0에서 n-1까지 반복해봅니다.
for num in range(n):
    # 별 *들이 오른쪽으로 정렬된 형태의 역삼각형을 출력해야합니다.
    # 먼저 공백을 현재 숫자만큼 출력하고, 다음 줄로 내리지 않습니다.
    print(' ' * num, end='')
    # 별 *들을 (n - 현재 숫자)만큼 출력합니다.
    print('*' * (n - num))
