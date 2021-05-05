# https://www.acmicpc.net/problem/15736

# 첫 번째 줄에 출전한 학생의 수이자, 깃발의 개수인 N을 입력합니다.
# 1 <= N <= 2,100,000,000
N = int(input())

flags = [False for flag in range(N)]

for flag_index in range(N):
    for student_index in range(1, N + 1):
        if (flag_index + 1) % student_index == 0:
            if flags[flag_index]:
                flags[flag_index] = False
            else:
                flags[flag_index] = True

white_flags_count = flags.count(True)

print(white_flags_count)