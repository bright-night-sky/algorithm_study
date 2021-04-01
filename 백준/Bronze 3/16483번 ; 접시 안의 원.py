# https://www.acmicpc.net/problem/16483

# 첫째 줄에 양의 정수 T를 입력합니다.
# T의 값은 10,000 이하입니다.
T = int(input())

# 그림을 그려보면
# a^2 - b^2 = (T/2)^2입니다.
result = (T / 2) ** 2

# 소수 자리가 있는 경우, 소수 첫째 자리에서 반올림해야합니다.
result = round(result)

# 결과를 출력합니다.
print(result)