# https://codeup.kr/problem.php?id=6021

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 5개의 문자로 이루어진 단어 1개를 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
word = stdin.readline().rstrip()

# 입력한 단어에서 한 글자씩 반복합니다.
for char in word:
    # 현재 글자를 출력합니다.
    print(char)