# https://codeup.kr/problem.php?id=6037

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 반복 횟수를 입력합니다.
# 정수형으로 변환합니다.
repeat = int(stdin.readline())
# 문장을 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
sentence = stdin.readline().rstrip()

# 입력한 횟수만큼 입력한 문장을 출력합니다.
print(sentence * repeat)