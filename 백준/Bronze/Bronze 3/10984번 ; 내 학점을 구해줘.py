# https://www.acmicpc.net/problem/10984

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 번째 줄에 학기의 수 T를 입력합니다.
# 정수형으로 변환합니다.
T = int(stdin.readline())

# 학기의 수 T만큼 반복합니다.
for semester_idx in range(T):
    # 과목의 수 N을 입력합니다.
    # 1 <= N <= 10
    # 정수형으로 변환합니다.
    N = int(stdin.readline())
    # 평점(GPA)를 저장할 변수를 선언합니다.
    # 0으로 초기화합니다.
    gpa = 0
    # 총 이수 학점을 저장할 변수를 선언합니다.
    # 0으로 초기화합니다.
    credits = 0

    # 과목의 수 N만큼 반복합니다.
    for subject_idx in range(N):
        # 이수 학점 C, 성적 G를 공백으로 구분해 입력합니다.
        # 1 <= C <= 6이고 정수입니다.
        # G는 {0, 0.7, 1, 1.3, 1.7, 2, 2.3, 2.7, 3, 3.3, 3.7, 4, 4.3} 중 하나입니다.
        C, G = stdin.readline().split()
        # 이수 학점 C는 정수형으로 변환합니다.
        C = int(C)
        # 성적 G는 실수형으로 변환합니다.
        G = float(G)

        # 총 이수 학점에 현재 과목의 이수 학점을 더해줍니다.
        credits += C
        # 평점에 현재 과목의 (이수 학점) X (성적)을 더해줍니다.
        gpa += C * G

    # 총점에 저장되어 있는 값을 총 이수 학점으로 나눠줍니다.
    gpa /= credits
    # 평점을 소수점 둘째 자리에서 반올림합니다.
    gpa = round(gpa, 1)

    # 출력 형식에 맞게 총 이수 학점과 평점을 공백으로 구분해 출력합니다.
    print(f'{credits} {gpa}')