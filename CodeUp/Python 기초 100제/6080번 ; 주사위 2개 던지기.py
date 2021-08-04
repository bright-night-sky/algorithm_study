# https://codeup.kr/problem.php?id=6080

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 서로 다른 주사위 2개의 면의 개수 n, m을 공백을 두고 입력합니다.
# 각각 정수형으로 변환합니다.
n, m = map(int, stdin.readline().split(' '))

# 첫 번째 수는 n의 수를 출력해야 하므로
# 면의 개수가 m인 주사위보다 더 나중에 반복문을 돌려야합니다.
# 그래서 바깥 for문에서 n 주사위에 대한 반복문을 돌립니다.
for n_num in range(1, n + 1):
    # 두 번째 수는 면의 수가 m인 주사위의 숫자를 오름차순 출력하는 것이므로
    # 면의 수가 n인 주사위보다 더 먼저 반복문을 돌려야합니다.
    # 그래서 안쪽 for문에서 m 주사위에 대한 반복문을 돌립니다.
    for m_num in range(1, m + 1):
        # 첫 번째 수는 n, 두 번재 수는 m으로 고정해 1부터 오름차순 순서로 출력합니다.
        print(n_num, m_num)