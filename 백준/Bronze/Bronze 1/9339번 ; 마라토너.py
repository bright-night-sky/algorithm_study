# https://www.acmicpc.net/problem/9339

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 테스트 케이스의 개수 T를 입력합니다.
# T <= 10
T = int(stdin.readline().rstrip())

# 테스트 케이스의 개수 T만큼 반복해봅니다.
for test_case_index in range(T):
    # 각 테스트 케이스의 첫째 줄에는 수강생의 수 K를 입력합니다.
    # 1 < K <= 100
    K = int(stdin.readline().rstrip())

    # 둘째 줄에는 수강생의 참가 번호를 공백으로 구분해 입력합니다.
    # 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
    students = list(map(int, stdin.readline().rstrip().split(' ')))

    # 셋째 줄에는 대회의 참가자 수 N을 입력합니다.
    # K < N <= 1,000
    N = int(stdin.readline().rstrip())

    # 학원 수강생을 포함한 모든 마라톤 참가자의 정보를 저장할 리스트 변수를 선언합니다.
    all_participant = []

    # 마라톤 대회 참가자 수 N만큼 반복해봅니다.
    for participant_index in range(N):
        # 각 참가자의 참가 번호, 기록 시, 분을 입력합니다.
        # 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
        participant_info = list(map(int, stdin.readline().rstrip().split(' ')))

        # 위의 한 참가자의 마라톤 기록을 저장한 리스트를 all_participant에 넣어줍니다.
        all_participant.append(participant_info)

    # all_participant에서 학원 수강생이고 마라톤 완주를 했으며 기록이 6시간 이하인 경우를 필터링한 결과를 저장하는 변수를 선언합니다.
    students_records = filter(lambda participant: participant[0] in students and participant[1] != -1 and (participant[1] <= 5 or (participant[1] == 6 and participant[2] == 0)), all_participant)

    # students_records에서 마라톤 기록인 시, 분을 기준으로 오름차순 정렬을 하고 난 뒤의 결과를 저장하는 변수를 선언합니다.
    fast_sorted_students = sorted(students_records, key=lambda student: (student[1], student[2]))

    # 문제에서 항상 대회 인증서를 받은 수강생이 존재한다고 하였습니다.
    # fast_sorted_students에서 맨 앞에 있는 수강생의 번호를 저장하는 변수를 선언합니다.
    fastest_student_num = fast_sorted_students[0][0]
    # 마라톤 대회에서 인증서를 받은 학생들의 수를 저장하는 변수를 선언합니다.
    recorded_students = len(fast_sorted_students)

    # 가장 기록이 좋은 수강생의 번호와 인증서를 받은 수강생의 수를 출력 형식에 맞게 출력합니다.
    print(fastest_student_num, recorded_students)