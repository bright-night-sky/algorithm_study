# https://www.acmicpc.net/problem/8932

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 트랙 경기와 필드 경기에서의 점수를 낼 때
# 각 종목마다의 A, B, C 상수들을 리스트 변수로 선언합니다.
A = [9.23076, 1.84523, 56.0211, 4.99087, 0.188807, 15.9803, 0.11193]
B = [26.7, 75, 1.5, 42.5, 210, 3.8, 254]
C = [1.835, 1.348, 1.05, 1.81, 1.41, 1.04, 1.88]

# 첫째 줄에 테스트 케이스의 개수 T를 입력합니다.
# 정수형으로 변환합니다.
T = int(stdin.readline())

# 테스트 케이스의 개수 T만큼 반복합니다.
for _ in range(T):
    # 종목별 기록인 일곱 개의 정수를 공백으로 구분해 입력합니다.
    # 각각 정수형으로 변환합니다.
    records = list(map(int, stdin.readline().split(' ')))
    # 총점을 저장할 변수를 선언합니다.
    total_score = 0

    # 각 종목에서 트랙인 경기와 필드인 경기의 인덱스들을 저장하는 변수를 선언합니다.
    track_index = [0, 3, 6]
    field_index = [1, 2, 4, 5]

    # 종목의 개수인 7만큼 반복합니다.
    for records_idx in range(8):
        # 현재 종목이 트랙 경기라면
        if records_idx in track_index:
            # 트랙 경기의 공식에 맞게 계산하는 변수를 선언합니다.
            # 소수 부분은 떼어줍니다.
            score = int(A[records_idx] * ((B[records_idx] - records[records_idx]) ** C[records_idx]))
            # 계산한 점수를 총점에 더해줍니다.
            total_score += score
        # 현재 종목이 필드 경기라면
        elif records_idx in field_index:
            # 필드 경기의 공식에 맞게 계산하는 변수를 선언합니다.
            # 소수 부분은 떼어줍니다.
            score = int(A[records_idx] * ((records[records_idx] - B[records_idx]) ** C[records_idx]))
            total_score += score

    # 총점을 출력합니다.
    print(total_score)