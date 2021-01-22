# https://www.acmicpc.net/problem/4766

# 이전의 온도를 저장할 변수
# 절대 나올 수 없는 온도인 -11로 초기화
prev_temperature = -11

while True:
    # 혼합물의 온도 입력
    # -10 <= 온도 <= 200
    # 소수점 둘째자리까지 적혀져 있을 수도 있다.
    temperature = float(input())

    # 만약 입력한 값이 999라면
    if temperature == 999:
        # 측정 종료
        break

    # 만약 이전 온도에 저장된 값이 -11이 아니라면
    if prev_temperature != -11:
        # 현재 온도와 이전 온도의 차이를 출력하는 변수
        # 항상 소수점 둘째 자리까지 출력한다.
        result = "%.2f" % round(temperature - prev_temperature, 2)
        print(result)
        # 현재 온도의 값을 이전 온도 변수에 저장
        prev_temperature = temperature
    else:
        # 한 번 더 실험을 해야하므로 현재 온도의 값을 이전 온도 변수에 저장
        prev_temperature = temperature
