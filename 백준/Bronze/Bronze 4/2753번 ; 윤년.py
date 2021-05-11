# https://www.acmicpc.net/problem/2753

# 연도 입력
# 1 <= 연도 <= 4000인 자연수
year = int(input())

# 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수이면
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    # 윤년이므로 1 출력
    print(1)
# 나머지는 윤년이 아니므로
else:
    # 0 출력
    print(0)