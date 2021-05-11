# https://www.acmicpc.net/problem/17173

# 첫 번째 줄에 N, M을 입력합니다.
# 2 <= N <= 1000
# 1 <= M < N
N, M = map(int, input().split(' '))

# M개의 정수 Ki들을 공백으로 구분해 입력합니다.
# 2 <= Ki <= 1000
# 각 정수 Ki들은 정수형으로 변환하고 리스트 변수에 넣어줍니다.
# 동일한 Ki는 없고, 오름차순으로 정렬되어 있습니다.
Kis = list(map(int, input().split(' ')))

# Ki 중 적어도 하나의 배수이면서 1 이상 N 이하인 수들의 합을 저장하는 변수를 선언합니다.
sum_num = 0

# Ki 중 가장 작은 값부터 N까지 반복해봅니다.
for number in range(Kis[0], N + 1):
    # Ki들의 값들 하나씩 반복해봅니다.
    for Ki in Kis:
        # 현재 숫자가 현재 Ki로 나누어진다면
        if number % Ki == 0:
            # sum_num에 현재 숫자를 더해줍니다.
            sum_num += number
            # Ki들 중 하나에만 나누어 떨어지면 되므로 조건을 만족했으니 조건문을 탈출합니다.
            # 만약 탈출하지 않으면 Ki들 중 여러 값에 나누어 떨어질 수 있을 때는 현재 숫자를 또 더하기 때문입니다.
            break

# sum_num의 값을 출력합니다.
print(sum_num)