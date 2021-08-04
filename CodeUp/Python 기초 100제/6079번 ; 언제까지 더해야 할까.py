# https://codeup.kr/problem.php?id=6079

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 정수 1개를 입력합니다.
# 정수형으로 변환합니다.
compare_num = int(stdin.readline())
# 1, 2, 3, ... 차례로 더한 값을 저장할 변수를 선언합니다.
# 0으로 초기화합니다.
num_sum = 0
# 1, 2, 3, ... 차례로 더해나갈 수를 저장하는 변수를 선언합니다.
# 1부터 시작하므로 1로 초기화합니다.
cur_num = 1

# 계속 반복하는 반복문을 만듭니다.
while True:
    # 차례로 더한 숫자의 합에 현재 반복 중인 숫자를 더합니다.
    num_sum += cur_num

    # 차례로 더한 숫자의 합이 입력한 정수보다 크거나 같다면
    if num_sum >= compare_num:
        # 현재 반복 중인 숫자를 출력합니다.
        print(cur_num)
        # 반복문을 탈출합니다.
        break

    # 현재 반복 중인 숫자에 1을 더합니다.
    cur_num += 1