# https://codeup.kr/problem.php?id=1212

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 직선의 길이 3개를 공백으로 구분해 입력합니다.
# 각각 int형으로 변환하고, 리스트 변수 sides에 넣어줍니다.
sides = list(map(int, stdin.readline().split()))
# sides에서 가장 긴 직선의 길이를 구하고 변수 max_len_side에 저장합니다.
max_len_side = max(sides)
# 모든 직선들의 길이의 합을 구하고 변수 sides_len_sum에 저장합니다.
sides_len_sum = sum(sides)
# 모든 직선들의 길이의 합에서 가장 긴 직선의 길이를 빼서
# 더 짧은 두 직선들의 길이의 합을 구해 변수 short_sides_len_sum에 저장합니다.
short_sides_len_sum = sides_len_sum - max_len_side

# 가장 긴 직선의 길이가 더 짧은 나머지 두 직선들의 길이의 합보다 작다면
if max_len_side < short_sides_len_sum:
    # 삼각형이 성립되므로, 문자열 'yes'를 출력합니다.
    print('yes')
# 그 외의 경우, 즉, 가장 긴 직선의 길이가 더 짧은 나머지 두 직선들의 길이의 합 이상이라면
else:
    # 삼각형이 성립되지 않으므로, 문자열 'no'를 출력합니다.
    print('no')