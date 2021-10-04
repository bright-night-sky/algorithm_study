# https://codeup.kr/problem.php?id=1366

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 사각형의 크기 n을 입력합니다.
# 3 <= n <= 99, n은 홀수입니다.
# int형으로 변환합니다.
n = int(stdin.readline())
# 사각형의 공백이 있는 한 줄에서 공백 개수의 절반을 저장할 변수를 선언합니다.
one_side_blank_cnt = (n - 5) // 2

# 사각형의 첫 번째 줄인 별 *을 n개만큼 출력합니다.
print('*' * n)

# 사각형의 첫 번째 줄과 가운데 줄 사이를 출력하는 부분입니다.
# 줄의 개수는 한 줄에서 공백 개수의 절반에 1을 더한 값입니다.
# 한 줄에서 첫 번째 별과 두 번째 별 사이 공백의 개수를 0 ~ one_side_blank_cnt까지 반복합니다.
for blank_cnt in range(one_side_blank_cnt + 1):
    # 별 하나를 출력하고, 다음 줄로 내리지 않습니다.
    print('*', end='')
    # 공백을 현재 숫자인 blank_cnt만큼 출력하고, 다음 줄로 내리지 않습니다.
    print(' ' * blank_cnt, end='')
    # 별 하나를 출력하고, 다음 줄로 내리지 않습니다.
    print('*', end='')
    # 공백을 one_side_blank_cnt에서 현재 숫자인 blank_cnt를 뺀 값만큼 출력하고, 다음 줄로 내리지 않습니다.
    print(' ' * (one_side_blank_cnt - blank_cnt), end='')
    # 별 하나를 출력하고, 다음 줄로 내리지 않습니다.
    print('*', end='')
    # 공백을 one_side_blank_cnt에서 현재 숫자인 blank_cnt를 뺀 값만큼 출력하고, 다음 줄로 내리지 않습니다.
    print(' ' * (one_side_blank_cnt - blank_cnt), end='')
    # 별 하나를 출력하고, 다음 줄로 내리지 않습니다.
    print('*', end='')
    # 공백을 현재 숫자인 blank_cnt만큼 출력하고, 다음 줄로 내리지 않습니다.
    print(' ' * blank_cnt, end='')
    # 별 하나를 출력하고, 다음 줄로 넘어갑니다.
    print('*')

# 사각형의 가운데 줄인 별 *을 n개만큼 출력합니다.
print('*' * n)

# 사각형의 가운데 줄과 마지막 줄 사이를 출력하는 부분입니다.
# 한 줄에서 두 번째 별과 세 번째 별 사이 공백의 개수를 0 ~ one_side_blank_cnt까지 반복합니다.
for blank_cnt in range(one_side_blank_cnt + 1):
    # 별 하나를 출력하고, 다음 줄로 내리지 않습니다.
    print('*', end='')
    # 공백을 one_side_blank_cnt에서 현재 숫자인 blank_cnt를 뺀 값만큼 출력하고, 다음 줄로 내리지 않습니다.
    print(' ' * (one_side_blank_cnt - blank_cnt), end='')
    # 별 하나를 출력하고, 다음 줄로 내리지 않습니다.
    print('*', end='')
    # 공백을 현재 숫자인 blank_cnt만큼 출력하고, 다음 줄로 내리지 않습니다.
    print(' ' * blank_cnt, end='')
    # 별 하나를 출력하고, 다음 줄로 내리지 않습니다.
    print('*', end='')
    # 공백을 현재 숫자인 blank_cnt만큼 출력하고, 다음 줄로 내리지 않습니다.
    print(' ' * blank_cnt, end='')
    # 별 하나를 출력하고, 다음 줄로 내리지 않습니다.
    print('*', end='')
    # 공백을 one_side_blank_cnt에서 현재 숫자인 blank_cnt를 뺀 값만큼 출력하고, 다음 줄로 내리지 않습니다.
    print(' ' * (one_side_blank_cnt - blank_cnt), end='')
    # 별 하나를 출력하고, 다음 줄로 넘어갑니다.
    print('*')

# 사각형의 마지막 줄인 별 *을 n개만큼 출력합니다.
print('*' * n)
