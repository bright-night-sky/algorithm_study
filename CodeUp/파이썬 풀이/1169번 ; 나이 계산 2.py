# https://codeup.kr/problem.php?id=1169

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 나이를 입력합니다.
# 113살 이하로만 입력합니다.
# 정수형으로 변환합니다.
age = int(stdin.readline())
# 2012년 기준이므로 2012에서 입력한 나이를 빼고 1을 더해 출생년도를 구하고 변수에 저장합니다.
birth_year = 2012 - age + 1
# 1900년대 출생인지 2000년대 출생인지를 저장할 변수를 선언합니다.
year_info = None

# 출생년도가 2000보다 작다면
if birth_year < 2000:
    # 1900년대 출생이므로 year_info에 1을 저장합니다.
    year_info = 1
# 그 외의 경우, 즉, 출생년도가 2000 이상이면
else:
    # 2000년대 출생이므로 year_info에 3을 저장합니다.
    year_info = 3

# 출생년도는 뒤의 두 자리만 출력해야 하므로,
# birth_year의 값을 100으로 나눈 나머지를 다시 birth_year에 저장합니다.
birth_year %= 100

# 출생년도 뒤의 두 자리와 연도정보를 공백으로 구분해 출력합니다.
print(birth_year, year_info)