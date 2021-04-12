# https://www.acmicpc.net/problem/17826

# 첫째 줄에는 홍익이의 점수를 포함한 학생들의 점수 50개가 띄어쓰기로 구분해 입력합니다.
# 점수는 내림차순으로 정렬되어 있습니다.
# 같은 점수는 없습니다.
# 각 점수들은 정수형 처리를 하고 리스트 변수 scores에 넣어줍니다.
scores = list(map(int, input().split(' ')))

# 둘째 줄에는 홍익이가 받은 점수를 입력합니다.
# 모든 점수들은 0 이상 300 이하의 정수입니다.
hongik_score = int(input())

# 홍익이의 등수를 저장하는 변수를 선언합니다.
hongik_rank = scores.index(hongik_score) + 1

# 홍익이의 등수가 1~5등이면
if 1 <= hongik_rank <= 5:
    # A+을 출력합니다.
    print('A+')
# 홍익이의 등수가 6~15등이면
elif 6 <= hongik_rank <= 15:
    # A0를 출력합니다.
    print('A0')
# 홍익이의 등수가 16~30등이면
elif 16 <= hongik_rank <= 30:
    # B+를 출력합니다.
    print('B+')
# 홍익이의 등수가 31~35등이면
elif 31 <= hongik_rank <= 35:
    # B0를 출력합니다.
    print('B0')
# 홍익이의 등수가 36~45등이면
elif 36 <= hongik_rank <= 45:
    # C+를 출력합니다.
    print('C+')
# 홍익이의 등수가 46~48등이면
elif 46 <= hongik_rank <= 48:
    # C0를 출력합니다.
    print('C0')
# 그 이하의 등수라면
else:
    # F를 출력합니다.
    print('F')