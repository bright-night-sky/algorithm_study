# https://www.acmicpc.net/problem/1977

# 첫째 줄에 M을 입력합니다.
M = int(input())

# 둘째 줄에 N을 입력합니다.
# M, N은 10000 이하의 자연수이며
# M은 N보다 같거나 작습니다.
N = int(input())

# 완전제곱수들을 저장할 리스트 변수를 선언합니다.
perfect_square_num = []

# M부터 N까지 반복해봅니다.
for number in range(M, N + 1):
    # 현재 숫자의 제곱근의 소수 부분을 저장하는 변수를 선언합니다.
    str_num_float = str(number ** 0.5).split('.')[1]

    # 제곱근의 소수 부분이 0이라면
    if str_num_float == '0':
        # 현재 숫자는 완전제곱수이므로 perfect_square_num에 넣어줍니다.
        perfect_square_num.append(number)

# 완전제곱수들의 합을 저장하는 변수를 선언합니다.
perfect_square_num_sum = sum(perfect_square_num)

# 완전제곱수들의 합이 0이라면
if perfect_square_num_sum == 0:
    # -1을 출력합니다.
    print(-1)
# 완전제곱수들의 합이 0보다 크다면
else:
    # 출력 형식에 맞게 완전제곱수들의 합과
    print(int(perfect_square_num_sum))
    # 완전제곱수들 중 가장 작은 수를 출력합니다.
    print(min(perfect_square_num))