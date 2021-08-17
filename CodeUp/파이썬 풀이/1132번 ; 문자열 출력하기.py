# https://codeup.kr/problem.php?id=1132

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 한 단어를 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
word = stdin.readline().rstrip()

# 입력한 단어를 그대로 출력합니다.
print(word)