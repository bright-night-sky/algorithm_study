# https://www.acmicpc.net/problem/11637

# 첫 번째 줄에 테스트 케이스의 수 T를 입력합니다.
# 1 < T < 500
T = int(input())

# 테스트 케이스의 수 T만큼 반복합니다.
for test_case_index in range(T):
    # 후보자의 수 n을 입력합니다.
    n = int(input())

    # 각 후보자들의 득표 수를 저장하는 리스트 변수를 선언합니다.
    candidates_votes = []

    # 후보자의 수 n만큼 반복합니다.
    for candidate_index in range(n):
        # 이번 후보자의 득표 수를 입력합니다.
        vote = int(input())

        # 이번 후보자의 득표 수를 candidates_votes에 넣어줍니다.
        candidates_votes.append(vote)

    # 총 득표수의 과반수를 저장하는 변수를 선언합니다.
    majority_votes = int(sum(candidates_votes) / 2)

    # 가장 많은 득표 수를 저장하는 변수를 선언합니다.
    max_voted_candidate = max(candidates_votes)
    # 가장 많은 득표 수를 얻은 후보자의 번호를 저장하는 변수를 선언합니다.
    max_voted_candidate_index = candidates_votes.index(max_voted_candidate) + 1

    # 가장 많은 득표 수를 가진 후보자가 2명 이상이라면
    if candidates_votes.count(max_voted_candidate) >= 2:
        # 최다 득표자가 없으므로 no winner를 출력합니다.
        print("no winner")
    # 가장 많은 득표 수를 가진 후보자가 1명이고
    else:
        # 최다 득표자의 득표 수가 과반수 초과라면
        if max_voted_candidate > majority_votes:
            # majority winner 최다 득표자의 번호 형식으로 출력합니다.
            print(f"majority winner {max_voted_candidate_index}")
        # 최다 득표자의 득표 수가 과반수 이하라면
        else:
            # minority winner 최다 득표자의 번호 형식으로 출력합니다.
            print(f"minority winner {max_voted_candidate_index}")