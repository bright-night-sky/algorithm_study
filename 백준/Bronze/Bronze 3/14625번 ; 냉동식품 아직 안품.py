# https://www.acmicpc.net/problem/14625

# 첫째 줄에 시작시간의 시와 분을 입력합니다.
start_H, start_M = map(int, input().split(' '))

# 둘째 줄에 종료시간의 시와 분을 입력합니다.
end_H, end_M = map(int,input().split(' '))

# 세 번째 줄에는 몇 분이 나오는지 알고 싶은 숫자 N을 입력합니다.
# 0 <= N <= 9
N = int(input())

# N을 가지고 있는 시간의 개수를 저장하는 변수입니다.
N_count = 0

# 시작시간부터 종료시간까지 1분씩 증가시키면서 N의 개수를 세어봅니다.
while True:
    if start_H == end_H and start_M == end_M:
        break

    # 현재 시간의 시와 분에서 N을 가지고 있다면
    if str(start_H).count(str(N)) or str(start_M).count(str(N)):
        # 1을 추가해줍니다.
        N_count += 1

    # 만약 현재 시간에서 분이 59분이면
    if start_M == 59:
        # 시에 1을 추가하고
        start_H += 1
        # 분은 다시 0으로 맞춰줍니다.
        start_M = 0
        continue

    # 1분을 추가해서 다음 시간으로 넘어갑니다.
    start_M += 1

# N을 가지고 있는 시간의 개수를 출력합니다.
print(N_count)