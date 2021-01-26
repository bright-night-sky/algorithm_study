# https://www.acmicpc.net/problem/17618

# 첫 번째 줄에 정수 N을 입력합니다.
# 1 <= N <= 10,000,000
N = int(input())

# 신기한 수의 개수를 저장하는 변수입니다.
amazing_count = 0

# 1부터 N까지 신기한 수의 조건에 부합하는지 알아봅니다.
for num in range(1, N+1):
    # 숫자를 문자형으로 바꿉니다.
    num = str(num)

    # 각 자리수의 숫자를 모두 더해서 저장하는 변수입니다.
    position_sum = 0

    # 각 자리수를 더해줍니다.
    for idx in range(0, len(num)):
        position_sum += int(num[idx])

    # 자릿수의 합이 현재 숫자를 나눌 수 있으면
    if int(num) % position_sum == 0:
        # 신기한 수이므로 신기한 수의 개수에 1을 더해줍니다.
        amazing_count += 1

# 신기한 수의 개수를 출력합니다.
print(amazing_count)