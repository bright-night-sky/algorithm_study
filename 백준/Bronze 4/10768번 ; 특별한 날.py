# https://www.acmicpc.net/problem/10768

# 첫 번째 줄은 1에서 12 사이의 월을 입력
month = int(input())
# 두 번째 줄은 1에서 31 사이의 그 달에 들어있는 날짜를 입력
day = int(input())

# 3월 이상인 경우
if month >= 3:
    # After 출력
    print("After")
# 2월인 경우
elif month == 2:
    # 2월 18일인 경우
    if day == 18:
        # Special 출력
        print("Special")
    # 2월 18일 후인 경우
    elif day > 18:
        # After 출력
        print("After")
    # 2월 18일 전인 경우
    else:
        # Before 출력
        print("Before")
# 1월인 경우
else:
    # Before 출력
    print("Before")