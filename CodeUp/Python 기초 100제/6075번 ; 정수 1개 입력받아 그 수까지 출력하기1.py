# https://codeup.kr/problem.php?id=6075

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 0 ~ 100 중 정수 1개를 입력합니다.
# 정수형으로 변환합니다.
num = int(stdin.readline())
# 0부터 입력한 정수까지 차례로 저장할 변수를 선언합니다.
# 0부터 출력하므로 0으로 초기화합니다.
cur_num = 0

# cur_num의 값이 num의 값보다 작거나 같으면 계속 반복합니다.
while cur_num <= num:
    # cur_num의 값을 출력합니다.
    print(cur_num)
    # cur_num에 1을 더하고 다시 저장합니다.
    cur_num += 1