# https://www.acmicpc.net/problem/16486

# 첫째 줄에 d1 입력
d1 = int(input())
# 둘째 줄에 d2 입력
d2 = int(input())
# d1, d2는 100,000 이하의 양의 정수

# 파이를 변수에 저장
pi = 3.141592

# 운동장의 반원 두 개를 합친 둘레
circle = 2 * d2 * pi

# 운동장의 직사각형 부분의 둘레 길이
rectangle = d1 * 2

# 총 둘레는 위의 두 변수의 값을 합친 것이다.
result = circle + rectangle

# 결과 출력
print(result)