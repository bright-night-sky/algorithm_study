# https://www.acmicpc.net/problem/15921

# 첫째 줄에 수찬이의 연습 기록 개수 N 입력
# 0 <= N <= 100
N = int(input())

# 만약 연습 기록이 하나도 없다면
if N == 0:
    # divde by zero 출력
    print("divide by zero")
# 연습 기록이 하나 이상 있다면
else:
    # 둘째 줄에 수찬이의 연습 기록 N개들 입력
    # N이 0이면 아무 입력 X
    # 연습 기록은 100 이하의 양의 정수
    practices = list(map(int, input().split(' ')))

    # 연습 기록들의 평균값을 저장하는 변수
    average = 0
    # 기댓값을 저장하는 변수
    expectation = 0
    # 결과인 연습과 비슷하게 꾸준한 기량을 뽐낼 수 있는 확률을 저장하는 변수
    result = 0

    # 일단 평균을 계산해서 average 변수에 저장
    average = sum(practices) / N

    # 기댓값 계산하기
    for practice in practices:
        expectation += practice * (1 / N)

    # 결과 계산하기
    result = average / expectation

    # 출력 양식에 맞게 소수 둘째 자리까지 출력하게 하기
    # 소수 셋째 자리에서 반올림을 해야한다.
    result = "%.2f" % round(result, 2)

    # 결과 출력하기
    print(result)
