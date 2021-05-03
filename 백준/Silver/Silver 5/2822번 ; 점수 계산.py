# https://www.acmicpc.net/problem/2822

# 입력할 점수들을 저장하는 리스트 변수를 선언합니다.
scores = []

# 문제 8개를 푸므로 8번 반복합니다.
for score_index in range(8):
    # 문제를 풀고 난 뒤의 점수 하나를 입력합니다.
    score = int(input())

    # 입력한 점수를 scores 리스트 변수에 넣어줍니다.
    scores.append(score)

# 점수들을 내림차순으로 정렬한 리스트 변수를 선언합니다.
sorted_scores = sorted(scores, reverse=True)

# 가장 높은 5개의 점수를 합한 변수를 선언합니다.
total = sum(sorted_scores[:5])
# 가장 높은 5개의 점수의 문제 번호를 저장하는 리스트 변수를 선언합니다.
max_scores_index = []

# 가장 높은 점수 5개의 문제 번호를 저장할 것이므로 5번 반복합니다.
for index in range(5):
    # 내림차순된 리스트 변수에서 현재 점수의 문제 번호를 저장하는 변수를 선언합니다.
    score_index = scores.index(sorted_scores[index]) + 1

    # max_scores_index에 위에서 저장한 문제 번호를 넣어줍니다.
    max_scores_index.append(score_index)

# 문제 번호가 증가하는 순서로 출력돼야하므로 오름차순으로 정렬해줍니다.
max_scores_index.sort()

# 참가자의 총점을 출력합니다.
print(total)
# 증가하는 순서로 문제 번호를 출력합니다.
for index in max_scores_index:
    print(index, end=' ')
