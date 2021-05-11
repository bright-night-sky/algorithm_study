# https://www.acmicpc.net/problem/14568

# 첫째 줄에 사탕의 총 개수 N을 입력합니다.
# 1 <= N <= 100
N = int(input())

# 영훈이, 남규, 택희가 가진 사탕의 개수를 저장하는 변수입니다.
# 일단 0으로 초기화해둡니다.
younghun = 0
namgyu = 0
taekhee = 0

# 사탕을 세 사람에게 분배하는 서로 다른 경우의 수를 저장하는 변수입니다.
# 규칙에 맞게 사탕을 분배하는 방법이 없다면 0을 출력해야하므로 0으로 초기화해둡니다.
case = 0

# 다른 사람이나 혼자만의 특별한 조건이 없는 영훈이 먼저 사탕을 분배해봅니다.
for i in range(1, N):
    younghun = i
    # 남규는 영훈이의 사탕 개수보다 2개 이상 더 많아야 하므로 남규에게 사탕을 나누어봅니다.
    for j in range(2, N):
        namgyu = younghun + j
        # 그리고 남은 사탕을 택희에게 줍니다.
        taekhee = N - namgyu - younghun

        # 만약 택희가 가진 사탕의 개수가 짝수이면
        if taekhee > 0 and taekhee % 2 == 0:
            # 경우의 수에 부합하므로 1을 더해줍니다.
            case += 1

# 사탕을 세 사람에게 분배하는 서로 다른 경우의 수를 출력합니다.
print(case)
