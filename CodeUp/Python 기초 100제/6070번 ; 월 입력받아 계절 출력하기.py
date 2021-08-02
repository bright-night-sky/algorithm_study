# https://codeup.kr/problem.php?id=6070

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 월을 의미하는 1개의 정수를 입력합니다.
# 1 ~ 12의 자연수입니다.
# 정수형으로 변환합니다.
month = int(stdin.readline())

# month의 값을 3으로 나누었을 때 몫이 0이거나 4라면
if month // 3 == 0 or month // 3 == 4:
    # 12, 1, 2월 중 하나이므로 겨울인 winter를 출력합니다.
    print("winter")
# month의 값을 3으로 나누었을 때 몫이 1이라면
elif month // 3 == 1:
    # 3, 4, 5월 중 하나이므로 봄인 spring을 출력합니다.
    print("spring")
# month의 값을 3으로 나누었을 때 몫이 2라면
elif month // 3 == 2:
    # 6, 7, 8월 중 하나이므로 여름인 summer를 출력합니다.
    print("summer")
# month의 값을 3으로 나누었을 때 몫이 3이라면
elif month // 3 == 3:
    # 9, 10, 11월 중 하나이므로 가을인 fall을 출력합니다.
    print("fall")