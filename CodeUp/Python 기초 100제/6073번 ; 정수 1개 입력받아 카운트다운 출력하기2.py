# https://codeup.kr/problem.php?id=6073

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 1 ~ 100 사이인 정수 1개를 입력합니다.
# 정수형으로 변환합니다.
num = int(stdin.readline())
# 입력한 정수에서 1을 뺀 값부터 카운타다운하므로
# num의 값에서 1을 빼고 다시 num에 넣어줍니다.
num -= 1

# num의 값이 -1이 아니라면 계속 반복합니다.
while num != -1:
    # num의 값을 출력합니다.
    print(num)
    # num의 값에서 1을 빼고 다시 num에 넣어줍니다.
    num -= 1