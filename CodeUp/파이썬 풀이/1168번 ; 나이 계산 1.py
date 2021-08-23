# https://codeup.kr/problem.php?id=1168

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 생년월일(6자리)과 성별정보(1자리)가 공백으로 구분해 입력합니다.
# 맨 끝의 \n은 떼어주고 각각 변수에 넣어줍니다.
birth, gender = stdin.readline().rstrip().split()
# birth에서 앞의 2자리가 년도 부분이므로 이를 정수로 변환하고 변수에 저장합니다.
year = int(birth[:2])
# 나이를 저장할 변수를 선언합니다.
# 처음에는 0으로 초기화합니다.
age = 0

# 성별정보가 1 혹은 2라면
if gender == '1' or gender == '2':
    # 1900년대에 출생한 사람이므로 year의 값에 1900을 더해줍니다.
    year += 1900
# 그 외의 경우, 즉, 성별정보가 3 혹은 4라면
else:
    # 2000년대에 출생한 사람이므로 year의 값에 2000을 더해줍니다.
    year += 2000

# 2012에서 년도를 빼주고 1을 더해 나이를 구하고 다시 변수 age에 저장합니다.
age = 2012 - year + 1

# 나이인 age의 값을 출력합니다.
print(age)