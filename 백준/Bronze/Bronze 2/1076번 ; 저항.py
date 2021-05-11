# https://www.acmicpc.net/problem/1076

# 저항의 값을 dictionary 자료형으로 저장
# 색: (값, 곱) 형태로 저장함
resistance = {
    'black': (0, 1),
    'brown': (1, 10),
    'red': (2, 100),
    'orange': (3, 1000),
    'yellow': (4, 10000),
    'green': (5, 100000),
    'blue': (6, 1000000),
    'violet': (7, 10000000),
    'grey': (8, 100000000),
    'white': (9, 1000000000)
}

# 색 3개 입력
first_value_color = input()
second_value_color = input()
multiple_color = input()

# 결과 출력
# 결과는 (첫 번째 색깔 값 * 10 + 두 번째 색깔 값) * 세 번째 색깔 곱
print((resistance[first_value_color][0] * 10 + resistance[second_value_color][0]) * resistance[multiple_color][1])