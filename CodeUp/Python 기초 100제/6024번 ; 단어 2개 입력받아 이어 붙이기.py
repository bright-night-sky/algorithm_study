# https://codeup.kr/problem.php?id=6024

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 알파벳과 숫자로 이루어진 2개의 단어를 공백으로 구분해 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
word1, word2 = stdin.readline().rstrip().split(' ')

# 입력한 2개의 단어를 순서대로 붙여서 출력합니다.
print(word1 + word2)