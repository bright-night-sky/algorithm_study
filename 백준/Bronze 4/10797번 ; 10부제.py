# https://www.acmicpc.net/problem/10797

# 첫 번째 줄에는 날짜의 일의 자리 숫자 입력
day_one = int(input())
# 두 번째 줄에는 5대의 자동차 번호의 일의 자리 숫자들을 공백으로 구분해서 입력
cars = list(map(int, input().split(' ')))
# 날짜와 자동차의 일의 자리 숫자는 모두 0 ~ 9의 정수이다.

# 입력한 날짜와 자동차의 번호가 같으면 10부제를 위반하는 것이다.
# 위반한 자동차의 수 출력
print(cars.count(day_one))