# https://codeup.kr/problem.php?id=6036

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 단어와 반복 횟수를 공백으로 구분해 입력합니다.
word, repeat_cnt = stdin.readline().split(' ')
# 반복 횟수는 정수형으로 변환합니다.
repeat_cnt = int(repeat_cnt)

# 입력한 단어를 입력한 횟수만큼 반복해 출력합니다.
print(word * repeat_cnt)