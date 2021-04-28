# https://www.acmicpc.net/problem/10822

# 첫째 줄에 문자열 S를 입력합니다.
# S의 길이는 최대 100입니다.
# 포함되어 있는 정수는 1,000,000보다 작거나 같은 자연수입니다.
S = input()

# 입력한 문자열 S를 ,로 구분해 숫자 형태로 리스트 변수에 넣어줍니다.
nums = list(map(int, S.split(',')))

# nums 리스트 변수에 있는 값들을 모두 더한 값을 출력합니다.
print(sum(nums))