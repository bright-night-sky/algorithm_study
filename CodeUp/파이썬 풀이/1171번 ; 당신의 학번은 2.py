# https://codeup.kr/problem.php?id=1171

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 학년, 반, 번호를 공백으로 구분해 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
grade, class_num, num = stdin.readline().rstrip().split()

# 반의 정수형 값이 10 미만이라면
if int(class_num) < 10:
    # 반의 문자열 값 앞에 문자 '0'을 붙여줍니다.
    class_num = '0' + class_num

# 번호의 정수형 값이 10 이상 100 미만이라면
if 10 <= int(num) < 100:
    # 번호의 문자열 값 앞에 문자 '0'을 붙여줍니다.
    num = '0' + num
# 번호의 정수형 값이 10 미만이라면
elif int(num) < 10:
    # 번호의 문자열 값 앞에 문자열 '00'을 붙여줍니다.
    num = '00' + num

# 학년, 반, 번호를 모두 붙여서 출력합니다.
print(grade + class_num + num)