# https://www.acmicpc.net/problem/17496

# 첫 번째 줄에 N, T, C, P 입력
# N : 여름의 일 수, 2 <= N <= 90
# T : 스타후르츠가 자라는데 걸리는 일 수, 1 <= T <= N-1
# C : 스타후르츠를 심을 수 있는 칸의 수, 1 <= C <= 300
# P : 스타후르츠 개당 가격, 1 <= P <= 1,000
# N, T, C, P는 모두 정수이다.
N, T, C, P = map(int, input().split(' '))

# 여름동안 스타후르츠를 몇 번 수확할 수 있는지 계산하고 저장하는 변수
starfruit_times = (N - 1) // T
# 한 번 심은 스타후르츠를 수확할 때 얻는 수익을 저장하는 변수
starfruit_one_turn = C * P

# 총 이익을 출력
print(starfruit_times * starfruit_one_turn)