# https://www.acmicpc.net/problem/5800

# 첫째 줄에 반의 수 K를 입력합니다.
# 1 <= K <= 100
K = int(input())

# 반의 수 K만큼 반복합니다.
for class_index in range(K):
    # 반의 학생수 N, 각 학생의 수학 성적을 공백으로 구분해 입력합니다.
    # 2 <= N <= 50
    # 시험 성적은 0보다 크거나 같고, 100보다 작거나 같은 정수입니다.
    N_and_scores = input().split(' ')

    # N과 학생들의 점수를 분리해줍니다.
    # 둘 다 정수형으로 변환해줍니다.
    N = int(N_and_scores[0])
    scores = list(map(int, N_and_scores[1:]))

    # 수학 성적 중 최고 점수를 저장하는 변수를 선언합니다.
    max_score = max(scores)
    # 수학 성적 중 최소 점수를 저장하는 변수를 선언합니다.
    min_score = min(scores)

    # 점수를 내림차순으로 정렬해줍니다.
    scores.sort(reverse=True)

    # 각 점수에서 인접한 점수와의 차이들을 저장하는 리스트 변수를 선언합니다.
    gaps = []

    # 점수에서 뒤에서 하나 뺀 것까지 반복합니다.
    for score_index in range(N - 1):
        # 점수 리스트 변수에서 현재 점수와 그 뒤의 인덱스에 있는 점수와의 차이를 저장하는 변수를 선언합니다.
        gap = scores[score_index] - scores[score_index + 1]

        # gaps에 위에서 구한 차이점을 넣어줍니다.
        gaps.append(gap)

    # gaps에서 최대 차이를 저장하는 변수를 선언합니다.
    largest_gap = max(gaps)

    # 출력 형식에 맞게 출력합니다.
    print(f"Class {class_index + 1}")
    print(f"Max {max_score}, Min {min_score}, Largest gap {largest_gap}")