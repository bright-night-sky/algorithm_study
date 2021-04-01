# https://www.acmicpc.net/problem/13410

# 첫째 줄에 단 N, 항 K를 입력합니다.
# 1 <= N, K <= 1,000인 자연수입니다.
N, K = map(int, input().split(' '))

# 거꾸로 구구단의 가장 큰 값을 저장할 변수 max_num을 만들어줍니다.
# 거꾸로 구구단에서의 각 값은 0보다 크므로 일단 0으로 초기화해줍니다.
max_num = 0

# 항 K만큼 반복해봅니다.
for i in range(K+1):
    # 구구단으로 계산하고 그 값을 뒤집어준 뒤에 다시 정수형으로 만들어 result 변수에 저장합니다.
    result = int(str(N * i)[::-1])

    # 현재 result의 값이 이전까지의 최댓값인 max_num보다 크다면
    if result > max_num:
        # max_num에 result의 값을 저장합니다.
        max_num = result

# 거꾸로 구구단의 가장 큰 값이 저장되어 있는 max_num의 값을 출력합니다.
print(max_num)