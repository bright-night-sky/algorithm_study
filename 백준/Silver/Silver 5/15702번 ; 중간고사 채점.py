# https://www.acmicpc.net/problem/15702

# 첫째 줄에 문제의 개수 N, 응시자의 수 M을 입력합니다.
# 1 <= N <= 100
# 1 <= M <= 100
N, M = map(int, input().split(' '))

# 둘째 줄에 문제의 배점을 1번 문제부터 N번 문제까지 공백으로 구분해 입력합니다.
# 각 문제의 배점은 100보다 작거나 같은 자연수입니다.
allot_points = list(map(int, input().split(' ')))

# 응시자들의 정보를 저장할 리스트 변수를 선언합니다.
examiners = []

# 응시자의 수 M만큼 반복해봅니다.
for examiner_index in range(M):
    # 응시자의 정보인 응시자의 수험 번호, 시험 문제의 채점 결과를 입력합니다.
    # 수험 번호는 100,000보다 작거나 같은 자연수입니다.
    # 시험 문제의 채점 결과는 'O', 'X' 중 하나입니다.
    examiner_info = input().split(' ')

    # 수험 번호는 정수형으로 변환해줍니다.
    examiner_info[0] = int(examiner_info[0])

    # 이번 응시자의 점수를 저장하는 변수를 선언합니다.
    examiner_score = 0

    # 문제의 개수 N만큼 반복해봅니다.
    for index in range(N):
        # 응시자가 이번 문제를 맞춘 경우
        if examiner_info[index+1] == 'O':
            # 해당 문제의 배점을 examiner_score에 더해줍니다.
            examiner_score += allot_points[index]

    # 이번 응시자의 정보 리스트 변수 맨 뒤에 응시자의 점수를 넣어줍니다.
    examiner_info.append(examiner_score)

    # 이번 응시자의 정보 리스트 값을 examiners에 넣어줍니다.
    examiners.append(examiner_info)

# 첫 번째로 응시자들의 점수를 기준으로 내림차순,
# 점수가 같은 응시자가 있다면 두 번째로 응시자들의 수험 번호를 기준으로 오름차순합니다.
examiners.sort(key=lambda examiner: (-examiner[-1], examiner[0]))

# 맨 앞에 있는 응시자의 수험 번호와 점수를 공백으로 구분해 출력합니다.
print(examiners[0][0], examiners[0][-1])