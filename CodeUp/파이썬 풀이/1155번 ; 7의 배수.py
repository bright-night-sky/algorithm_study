# https://codeup.kr/problem.php?id=1155

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 자연수를 하나 입력합니다.
# 정수형으로 변환합니다.
num = int(stdin.readline())

# 입력한 자연수가 7의 배수 즉, 7로 나누었을 때 나머지가 0이라면
if num % 7 == 0:
    # multiple을 출력합니다.
    print('multiple')
# 입력한 자연수가 7의 배수가 아니라면, 즉, 7로 나누었을 때 나머지가 0이 아니라면
else:
    # not multiple을 출력합니다.
    print('not multiple')