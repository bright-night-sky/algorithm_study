# https://www.acmicpc.net/problem/4344

# 첫째 줄에 테스트 케이스의 개수 C를 입력합니다.
C = int(input())

# 테스트 케이스의 수 C만큼 반복해봅니다.
for test_case_idx in range(C):
    # 학생의 수 N, N명의 점수를 공백으로 구분해 입력합니다.
    test_case = input().split(' ')
    # 학생의 수 N과 N명의 점수를 분리해서 각각 변수를 선언해 저장합니다.
    # 모든 값을 정수르 변환합니다.
    N = int(test_case[0])
    scores = list(map(int, test_case[1:]))

    # 평균을 구하는 변수를 선언합니다.
    avg = sum(scores) / N

    # 평균 점수보다 높은 점수만 필터링하여 저장하는 리스트 변수를 선언합니다.
    exceed_scores = list(filter(lambda score: score > avg, scores))
    # 평균 점수보다 높은 점수들의 개수를 저장하는 변수를 선언합니다.
    exceed_scores_count = len(exceed_scores)

    # 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력합니다.
    print("{:.3f}%".format(round(exceed_scores_count / N * 100, 3)))