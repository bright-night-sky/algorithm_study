# https://www.acmicpc.net/problem/1871

# 첫째 줄에 번호판의 수 N을 입력합니다.
# 1 <= N <= 100
N = int(input())

# 번호판의 수 N만큼 반복합니다.
for license_plate_index in range(N):
    # 번호판을 하나 입력합니다.
    # -로 구분해서 영어 대문자로 이루어진 첫 번째 부분, 숫자로 이루어진 부분으로 변수를 선언해 저장합니다.
    first_part, second_part = input().split('-')

    # 두 번째 부분의 가치인 정수형으로 변환합니다.
    second_part_value = int(second_part)

    # 첫 번째 부분의 가치를 저장하는 변수를 선언합니다.
    first_part_value = 0

    # 첫 번째 부분을 뒤집어줍니다.
    first_part = first_part[::-1]

    # 첫 번째 부분의 길이만큼 반복합니다.
    for index in range(len(first_part)):
        # 첫 번째 부분의 가치를 26진법 수처럼 계산합니다.
        # 첫 번째 부분을 거꾸로 뒤집어 줬으므로 26^0, 26^1, 26^3, ... 순으로 더하면 됩니다.
        first_part_value += (ord(first_part[index]) - 65) * (26 ** index)

    # |첫 번째 부분의 가치 - 두 번째 부분의 가치|가 100 이하라면
    if abs(first_part_value - second_part_value) <= 100:
        # nice를 출력합니다.
        print("nice")
    # 그 외의 값이라면
    else:
        # not nice를 출력합니다.
        print("not nice")