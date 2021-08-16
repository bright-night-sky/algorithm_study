# https://codeup.kr/problem.php?id=1127

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 중간고사 반영비율, 중간고사 점수를 공백으로 구분해 입력합니다.
# 각각 실수형으로 변환합니다.
midterm_ratio, midterm_score = map(float, stdin.readline().split())
# 기말고사 반영비율, 기말고사 점수를 공백으로 구분해 입력합니다.
# 각각 실수형으로 변환합니다.
finals_ratio, finals_score = map(float, stdin.readline().split())
# 수행평가 반영비율, 수행평가 점수를 공백으로 구분해 입력합니다.
# 각각 실수형으로 변환합니다.
perform_ratio, perform_score = map(float, stdin.readline().split())
# 각 점수들은 정수형으로 입력하는데, 어차피 실수형인 반영비율과 곱해야하므로
# 그냥 실수형으로 변환한 것입니다.

# 각 점수와 점수에 해당하는 반영비율로 총 점수를 계산합니다.
total = midterm_ratio * midterm_score + finals_ratio * finals_score + perform_ratio * perform_score

# 총 점수를 소수 첫째 자리까지 출력합니다.
print('%.1f' % total)