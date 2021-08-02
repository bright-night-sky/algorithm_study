# https://codeup.kr/problem.php?id=6069

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 영문자 1개를 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
char = stdin.readline().rstrip()

# 영문자가 A라면
if char == 'A':
    # best!!!를 출력합니다.
    print('best!!!')
# 영문자가 B라면
elif char == 'B':
    # good!!를 출력합니다.
    print('good!!')
# 영문자가 C라면
elif char == 'C':
    # run!을 출력합니다.
    print('run!')
# 영문자가 D라면
elif char == 'D':
    # slowly~를 출력합니다.
    print('slowly~')
# 그 외의 나머지 문자라면
else:
    # what?을 출력합니다.
    print('what?')