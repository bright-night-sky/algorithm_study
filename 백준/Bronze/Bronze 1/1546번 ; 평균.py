# https://www.acmicpc.net/problem/1546

# 첫째 줄에 시험 본 과목의 개수 N을 입력합니다.
# N은 1000보다 작거나 같습니다.
N = int(input())

# 둘째 줄에 세준이의 각 과목의 성적을 공백으로 구분해 입력합니다.
# 각 성적은 100보다 작거나 같은 음이 아닌 정수이고,
# 적어도 하나의 값은 0보다 큽니다.
# 각 성적을 정수형으로 변환하고 리스트 변수에 넣어줍니다.
scores = list(map(int, input().split(' ')))

# 입력한 성적 중 최댓값을 저장하는 변수를 선언합니다.
max_score = max(scores)

# 조작한 점수를 저장할 리스트 변수를 선언합니다.
new_scores = []

# 기존의 성적을 하나씩 반복해봅니다.
for score in scores:
    # 문제에 나온 식대로 각 성적의 조작한 결과를 저장하는 변수를 선언합니다.
    new_score = score / max_score * 100

    # 조작한 성적을 new_scores에 넣어줍니다.
    new_scores.append(new_score)

# 조작한 성적들의 평균을 출력합니다.
print(sum(new_scores) / N)