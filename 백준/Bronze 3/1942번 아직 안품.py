# https://www.acmicpc.net/problem/1942

# 세 개의 입력
for i in range(0, 3):
    # 한 줄에 시작하는 시각, 끝나는 시각 입력
    start_time, end_time = input().split(' ')
    # 3의 배수의 갯수를 저장할 변수
    count = 0

    # 시작하는 시각과 끝나는 시각에 콜론(:)을 떼어내고 숫자로 만들기
    start_time = start_time.replace(':', '')
    start_time = int(start_time)
    end_time = end_time.replace(':', '')
    end_time = int(end_time)

    # 시작하는 시간과 끝나는 시간 중 더 작은 값을 시작하는 시간, 더 큰 값을 끝나는 시간 변수에 넣음
    if start_time > end_time:
        start_time, end_time = end_time, start_time

    # 시작하는 시간부터 끝나는 시간 숫자까지 3의 배수 갯수 세기
    # 끝나는 시간 숫자도 포함해야한다.
    for i in range(start_time, end_time+1):
        if i % 3 == 0:
            count += 1

    # 카운팅한 3의 배수를 출력
    print(count)