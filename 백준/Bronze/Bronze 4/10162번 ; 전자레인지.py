# https://www.acmicpc.net/problem/10162

# 요리해야할 시간 T 입력 : 초 단위
# 1 <= T <= 10,000
T = int(input())

# 각 버튼을 눌렀을 때 올라가는 시간을 초로 환산한 변수
# A 버튼 : 5분 => 300초
A = 300
# B 버튼 : 1분 => 60초
B = 60
# C 버튼 : 10초
C = 10

# A 버튼이 필요한 횟수
A_count = T // A
# T 시간에서 A 버튼을 누른만큼 뺀다.
T -= 300 * A_count

# B 버튼이 필요한 횟수
B_count = T // B
# T 시간에서 B 버튼을 누른만큼 뺀다.
T -= 60 * B_count

# C 버튼이 필요한 횟수
C_count = T // C
# T 시간에서 C 버튼을 누른만큼 뺀다.
T -= 10 * C_count

# 만약 최종적으로 줄어든 시간이 0초가 아닌 경우
if T != 0:
    print(-1)
# 만약 최종적으로 줄어든 시간이 0초인 경우
else:
    # 최소 버튼 조작의 A, B, C 횟수를 차례대로 출력
    print(A_count, B_count, C_count)