# https://codeup.kr/problem.php?id=6087

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 1 ~ 100 중 정수 1개를 입력합니다.
# 정수형으로 변환합니다.
num = int(stdin.readline())

# 1부터 num + 1까지 반복합니다.
for cur_num in range(1, num + 1):
    # 현재 숫자가 3의 배수라면
    if cur_num % 3 == 0:
        # 이하 반복문 코드를 무시하고 다음 숫자로 넘어갑니다.
        continue

    # 현재 숫자를 출력하고 한 칸 띄어줍니다.
    print(cur_num, end=' ')