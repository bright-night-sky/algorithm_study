# https://www.acmicpc.net/problem/17072

# Intensity function을 구현합니다.
# 0 이상 255 이하의 정수값 r, g, b를 받습니다.
def intensity(r, g, b):
    # intensity는 2126R + 7152G + 722B의 결과값입니다.
    i = 2126 * r + 7152 * g + 722 * b

    # intensity가 0 이상 510,000 미만이라면
    if 0 <= i < 510000:
        # #을 반환합니다.
        return '#'
    # intensity가 510,000 이상 1,020,000 미만이라면
    elif 510000 <= i < 1020000:
        # 소문자 o를 반환합니다.
        return 'o'
    # intensity가 1,020,000 이상 1,530,000 미만이라면
    elif 1020000 <= i < 1530000:
        # +를 반환합니다.
        return '+'
    # intensity가 1,530,000 이상 2,040,000 미만이라면
    elif 1530000 <= i < 2040000:
        # -를 반환합니다.
        return '-'
    # intensity가 2,040,000 이상이라면
    elif 2040000 <= i:
        # .을 반환합니다.
        return '.'

# 첫 줄에 그림의 세로의 길이 N, 가로의 길이 M을 공백으로 구분해 입력합니다.
# 1 <= N, M <= 400
N, M = map(int, input().split(' '))

# 세로의 길이 N만큼 가로줄을 반복합니다.
for i in range(N):
    # 3M개의 정수를 공백으로 구분해 입력합니다.
    # 리스트 변수에 넣어줍니다.
    row = list(map(int, input().split(' ')))

    # 입력받은 한 줄의 값을 3개씩 잘라서 반복합니다.
    for j in range(0, len(row) - 2, 3):
        # 세 개의 정수를 Intensity function에 넣어 반환되는 값을 출력합니다.
        print(intensity(row[j], row[j+1], row[j+2]), end='')

    # 한 줄의 출력이 끝나면 다음 줄로 넘어갑니다.
    print()