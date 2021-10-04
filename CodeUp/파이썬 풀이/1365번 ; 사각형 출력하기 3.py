# https://codeup.kr/problem.php?id=1365

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 사각형의 크기 n을 정수로 입력합니다.
# 3 <= n <= 100
# int형으로 변환합니다.
n = int(stdin.readline())
# 가운데 줄을 제외한 공백이 있는 줄에서 공백의 개수를 저장하는 변수를 선언합니다.
blank_cnt = n - 4

# 사각형의 첫 번째 줄인 별 *를 n개만큼 출력합니다.
print('*' * n)

# 사각형의 첫 번째 줄부터 가운데 줄 사이를 출력하는 부분입니다.
# 한 줄에서 첫 번째 별과 두 번째 별 사이 공백의 개수를 0 ~ blank_cnt // 2까지 반복합니다.
for side_blank_cnt in range(blank_cnt // 2 + 1):
    # 별 하나를 출력하고 다음 줄로 내리지 않습니다.
    print('*', end='')
    # 공백을 현재 숫자인 side_blank_cnt만큼 출력하고, 다음 줄로 내리지 않습니다.
    print(' ' * side_blank_cnt, end='')
    # 별 하나를 출력하고 다음 줄로 내리지 않습니다.
    print('*', end='')
    # 두 번째 별과 세 번째 별 사이 공백의 개수는 blank_cnt에서
    # 첫 번째 별과 두 번째 별 사이의 공백 개수, 세 번째 별과 네 번째 별 사이의 공백 개수 합을
    # 뺀 것이므로 그만큼 공백을 출력하고, 다음 줄로 내리지 않습니다.
    print(' ' * (blank_cnt - side_blank_cnt * 2), end='')
    # 별 하나를 출력하고 다음 줄로 내리지 않습니다.
    print('*', end='')
    # 공백을 현재 숫자인 side_blank_cnt만큼 출력하고, 다음 줄로 내리지 않습니다.
    print(' ' * side_blank_cnt, end='')
    # 별 하나를 출력하고 다음 줄로 넘어갑니다.
    print('*')

# 사각형의 길이가 홀수인 경우 가운데 줄을 출력합니다.
if n % 2 == 1:
    # 별 * 3개 사이의 공백 개수는 blank_cnt를 2로 나누고 1을 더한 값입니다.
    # 출력 형식에 맞게 *(공백)*(공백)*을 출력합니다.
    print(f'*{" " * (blank_cnt // 2 + 1)}*{" " * (blank_cnt // 2 + 1)}*')

# 사각형의 가운데 줄과 마지막 줄 사이를 출력하는 부분입니다.
# 한 줄에서 첫 번째 별과 두 번째 별 사이 공백의 개수를 blank_cnt // 2부터 0까지 반복합니다.
for side_blank_cnt in range(blank_cnt // 2, -1, -1):
    # 별 하나를 출력하고 다음 줄로 내리지 않습니다.
    print('*', end='')
    # 공백을 현재 숫자인 side_blank_cnt만큼 출력하고, 다음 줄로 내리지 않습니다.
    print(' ' * side_blank_cnt, end='')
    # 별 하나를 출력하고 다음 줄로 내리지 않습니다.
    print('*', end='')
    # 두 번째 별과 세 번째 별 사이 공백의 개수는 blank_cnt에서
    # 첫 번째 별과 두 번째 별 사이의 공백 개수, 세 번째 별과 네 번째 별 사이의 공백 개수 합을
    # 뺀 것이므로 그만큼 공백을 출력하고, 다음 줄로 내리지 않습니다.
    print(' ' * (blank_cnt - side_blank_cnt * 2), end='')
    # 별 하나를 출력하고 다음 줄로 내리지 않습니다.
    print('*', end='')
    # 공백을 현재 숫자인 side_blank_cnt만큼 출력하고, 다음 줄로 내리지 않습니다.
    print(' ' * side_blank_cnt, end='')
    # 별 하나를 출력하고 다음 줄로 넘어갑니다.
    print('*')

# 사각형의 마지막 줄인 별 *를 n개만큼 출력합니다.
print('*' * n)
