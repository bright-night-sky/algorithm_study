# https://www.acmicpc.net/problem/1427

# 첫째 줄에 정렬하고자하는 수 N을 입력합니다.
# 1,000,000,000보다 작거나 같은 자연수입니다.
# 숫자 하나하나를 리스트 변수에 넣어줍니다.
N = list(input())

# N을 내림차순으로 정렬합니다.
N.sort(reverse=True)

# 내림차순한 N을 문자열 형태로 출력합니다.
print(''.join(N))