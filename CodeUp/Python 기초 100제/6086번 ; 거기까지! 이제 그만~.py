# https://codeup.kr/problem.php?id=6086

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 언제까지 합을 계산할 지를 정하는 정수 1개를 입력합니다.
# 정수형으로 변환합니다.
sum_limit = int(stdin.readline())
# 1, 2, 3, 4, 5, ... 순서대로 계속 더한 값을 저장할 변수를 선언합니다.
# 0으로 초기화합니다.
num_sum = 0
# 1, 2, 3, 4, 5, ... 순서대로 증가하는 수를 저장하는 변수를 선언합니다.
# 1부터 시작하므로 1로 초기화합니다.
cur_num = 1

# 계속 반복해봅니다.
while True:
    # 1, 2, 3, ... 차례로 더한 값이 sum_limit보다 크거나 같다면
    if num_sum >= sum_limit:
        # num_sum의 값을 출력합니다.
        print(num_sum)
        # 반복문을 탈출합니다.
        break

    # num_sum에 현재 숫자인 cur_num의 값을 더합니다.
    num_sum += cur_num
    # cur_num에 1을 더해 다음 숫자로 넘어갑니다.
    cur_num += 1