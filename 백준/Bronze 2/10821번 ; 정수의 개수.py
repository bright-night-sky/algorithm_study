# https://www.acmicpc.net/problem/10821

# 첫째 줄에 문자열 S를 입력합니다.
# S의 길이는 최대 100자입니다.
S = input()

# S를 ,로 구분해 리스트 변수에 저장합니다.
numbers = S.split(',')

# 리스트 변수의 길이값이 정수의 개수이므로 그 값을 출력합니다.
print(len(numbers))