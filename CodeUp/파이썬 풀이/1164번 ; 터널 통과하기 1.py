# https://codeup.kr/problem.php?id=1164

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 터널의 높이 3개를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
tunnel1, tunnel2, tunnel3 = map(int, stdin.readline().split())

# 입력한 터널의 높이 3개 중 하나라도 170 이하가 있다면
if tunnel1 <= 170 or tunnel2 <= 170 or tunnel3 <= 170:
    # "CRASH"를 출력합니다.
    print('CRASH')
# 그 외의 경우, 즉, 모든 터널의 높이가 170 초과이면
else:
    # "PASS"를 출력합니다.
    print('PASS')