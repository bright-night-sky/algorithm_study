# https://www.acmicpc.net/problem/16199

# 첫째 줄에 어떤 사람이 태어난 연도, 월, 일 입력
# 공백으로 구분, 항상 올바른 날짜만 입력
birth_year, birth_month, birth_day = map(int, input().split(' '))

# 둘째 줄에 기준 날짜 입력
# 공백으로 구분, 항상 올바른 날짜만 입력
# 연도는 1900년보다 크거나 같고, 2100년보다 작거나 같다.
year, month, day = map(int, input().split(' '))

# 만 나이, 세는 나이, 연 나이를 저장하는 변수
man_old = 0
count_old = 0
year_old = 0

# 만 나이 계산하기
# 기준 날짜의 월이 태어난 날짜의 월보다 큰 경우
if month > birth_month:
    # 만 나이는 (기준 년도) - (태어난 년도)
    man_old = year - birth_year
# 기준 날짜의 월이 태어난 날짜의 월과 같은 경우 : 일도 비교해봐야한다.
elif month == birth_month:
    # 기준 날짜의 일이 태어난 날짜의 일보다 크거나 같은 경우
    if day >= birth_day:
        # 만 나이는 (기준 년도) - (태어난 년도)
        man_old = year - birth_year
    # 기준 날짜의 일이 태어난 날짜의 일보다 작은 경우
    else:
        # 만 나이는 (기준 년도) - (태어난 년도) - 1
        man_old = year - birth_year - 1
# 기준 날짜의 월이 태어난 날짜의 월보다 작은 경우
else:
    # 만 나이는 (기준 년도) - (태어난 년도) - 1
    man_old = year - birth_year - 1

# 세는 나이 계산하기
count_old = year - birth_year + 1

# 연 나이 계산하기
year_old = year - birth_year

# 만 나이, 세는 나이, 연 나이를 한 줄씩 출력
print(man_old)
print(count_old)
print(year_old)