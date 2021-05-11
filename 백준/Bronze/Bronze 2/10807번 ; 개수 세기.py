# https://www.acmicpc.net/problem/10807

# 첫째 줄에 정수의 개수 N을 입력합니다.
# 1 <= N <= 100
N = int(input())

# 둘째 줄에는 정수를 공백으로 구분해 입력합니다.
numbers = list(map(int, input().split(' ')))

# 셋째 줄에는 찾으려고 하는 정수 v를 입력합니다.
v = int(input())
# 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같습니다.

# numbers에서 v의 개수를 저장하는 변수를 선언합니다.
v_count = numbers.count(v)

# v의 개수를 출력합니다.
print(v_count)