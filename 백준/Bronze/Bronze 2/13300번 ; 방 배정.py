# https://www.acmicpc.net/problem/13300

# 올림 함수 ceil을 사용하기 위해 import 해줍니다.
from math import ceil

# 첫 번째 줄에는 수학여행에 참가하는 학생 수인 정수 N,
# 한 방에 배정할 수 있는 최대 인원 수 K를 공백으로 분리해 입력합니다.
# 1 <= N <= 1,000
# 1 < K <= 1,000
N, K = map(int, input().split(' '))

# 인덱스 0에서 5까지를 1학년에서 6학년이라고 생각하고
# 그 안에 [0, 0]인 리스트를 만들어
# 이 리스트의 0번 인덱스의 값은 여학생의 수를,
# 1번 인덱스의 값은 남학생의 수를 가리키는 student_count 리스트 변수를 만들어 줍니다.
student_count = [[0, 0] for i in range(6)]

# N개의 줄을 입력해야 하므로 N만큼 반복합니다.
for i in range(N):
    # 학생의 성별 S, 학년 Y를 공백으로 분리해 입력합니다.
    # 성별 S는 0이면 여학생, 1이면 남학생입니다.
    # 1 <= Y <= 6
    S, Y = map(int, input().split(' '))

    # 입력한 성별과 학년에 속하는 student_count의 인덱스에 학생 수 한 명을 추가해줍니다.
    student_count[Y-1][S] += 1

# 필요한 최소한의 방의 개수를 저장할 변수를 만들어줍니다.
rooms = 0

# student_count에서 1학년에서 6학년까지
for grade in student_count:
    # 그리고 해당 학년의 여학생 수, 남학생 수를 저장한 리스트를 반복문을 이용해 접근합니다.
    for people in grade:
        # 해당 학년, 성별의 사람 수를 한 방에 배정할 수 있는 촤대 인원수 K로 나누고
        # 그 값을 소수 첫째 자리에서 올림하여
        # 해당 학년, 성별에서 필요한 최소한의 방의 개수를 구합니다.
        # 그리고 그 값을 rooms에 더해줍니다.
        rooms += ceil(people / K)

# 필요한 최소한의 방의 개수를 저장한 변수 rooms의 값을 출력합니다.
print(rooms)