# https://codeup.kr/problem.php?id=1156

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 자연수 하나를 입력합니다.
# 정수형으로 변환합니다.
num = int(stdin.readline())

# 입력한 자연수가 홀수이면, 즉, 2로 나누었을 때 나머지가 1이라면
if num % 2 == 1:
    # odd를 출력합니다.
    print('odd')
# 그 외의 경우인 입력한 자연수가 짝수라면, 즉, 2로 나누었을 때 나머지가 0이라면
else:
    # even을 출력합니다.
    print('even')