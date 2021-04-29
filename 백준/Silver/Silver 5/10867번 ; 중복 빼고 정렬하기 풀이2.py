# https://www.acmicpc.net/problem/10867

# 첫째 줄에 수의 개수 N을 입력합니다.
# 1 <= N <= 100,000
N = int(input())

# 둘째 줄에 숫자들을 공백으로 구분해 입력합니다.
# 숫자들은 절댓값이 1,000 보다 작거나 같은 정수입니다.
# 중복된 값을 없애기 위해 set 변수로 저장합니다.
numbers = list(set(map(int, input().split(' '))))

# numbers 리스트 변수 내부의 숫자들을 오름차순으로 정렬합니다.
numbers.sort()
# numbers 리스트 변수 내부의 숫자들을 문자열 형태로 저장합니다.
numbers = list(map(str, numbers))

# 숫자들을 공백으로 구분해 출력합니다.
print(' '.join(numbers))