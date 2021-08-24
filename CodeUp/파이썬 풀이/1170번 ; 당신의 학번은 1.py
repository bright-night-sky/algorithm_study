# https://codeup.kr/problem.php?id=1170

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 학년, 반, 번호를 공백으로 구분해 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
grade, class_num, num = stdin.readline().rstrip().split()

# 정수형의 번호가 10 미만일 때는
if int(num) < 10:
    # 문자열 형태의 번호 앞에 0을 붙입니다.
    num = '0' + num

# 학년, 반, 번호를 붙여 출력합니다.
print(grade + class_num + num)