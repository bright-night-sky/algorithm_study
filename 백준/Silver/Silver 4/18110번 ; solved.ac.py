# https://www.acmicpc.net/problem/18110

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 파이썬의 round 함수말고 우리가 일반적으로 사용하는 반올림을 하는 함수를 구현합니다.
# 소수 첫째 자리에서 반올림을 하는 함수입니다.
# 매개변수로 숫자 하나를 입력받습니다.
def normal_round(num):
    # 매개변수의 숫자와 그 숫자를 정수형으로 변환했을 때의 숫자의 차이가 0.5 이상이면
    if num - int(num) >= 0.5:
        # 정수형으로 변환한 숫자에 1을 더한 후 반환합니다.
        return int(num) + 1
    # 매개변수의 숫자와 그 숫자를 정수형으로 변환했을 때의 숫자의 차이가 0.5 미만이면
    else:
        # 정수형으로 변환한 숫자를 반환합니다.
        return int(num)

# 첫 번째 줄에 난이도 의견의 개수 n을 입력합니다.
# 0 <= n <= 3 X 10^5
n = int(stdin.readline())

# 난이도 의견의 개수 n이 0이라면
if n == 0:
    # 문제의 난이도는 0으로 결정하므로 0을 출력합니다.
    print(0)
# 난이도 의견의 개수 n이 1 이상이라면
else:
    # 입력받은 난이도 의견들을 저장할 리스트 변수를 선언합니다.
    difficulties = []

    # 난이도 의견의 개수 n만큼 반복합니다.
    for _ in range(n):
        # 난이도 의견 하나를 입력하고 정수형으로 변환합니다.
        # 난이도 의견은 1 이상 30 이하입니다.
        difficulty = int(stdin.readline())
        # 입력한 난이도 의견을 difficulties에 넣어줍니다.
        difficulties.append(difficulty)

    # difficulties에 있는 난이도 의견들을 오름차순으로 정렬해줍니다.
    difficulties.sort()

    # 위에서 15%, 아래에서 15%를 떼어내야 하므로
    # 현재 난이도 의견 개수에서 위, 아래로 얼마만큼 떼어내야 하는지를 저장하는 변수를 선언합니다.
    truncated_mean_limit = normal_round(n * 0.15)

    # 만약 truncated_mean_limit이 0이 아니라면
    if truncated_mean_limit != 0:
        # difficulties에서 위, 아래로 15%씩 떼어줍니다.
        difficulties = difficulties[truncated_mean_limit:-truncated_mean_limit]
    # 만약 truncated_mean_limit이 0이라면 떼어내는게 없습니다.

    # 문제의 난이도인 30% 절사평균을 계산해서 저장하는 변수를 선언합니다.
    truncated_mean = normal_round(sum(difficulties) / (n - truncated_mean_limit * 2))

    # 문제의 난이도를 출력합니다.
    print(truncated_mean)