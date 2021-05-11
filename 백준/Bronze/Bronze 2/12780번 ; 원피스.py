# https://www.acmicpc.net/problem/12780

# 첫 줄에 문자열 H를 입력합니다.
# 0 < |H| <= 100,000
H = input()

# 두 번째 줄에는 문자열 N을 입력합니다.
# 0 < |N| <= 10
N = input()
# H, N은 공백 없는 대문자 문자열입니다.

# H에서 N의 등장 횟수를 N_count 변수에 저장합니다.
N_count = H.count(N)

# N_count의 값을 출력합니다.
print(N_count)