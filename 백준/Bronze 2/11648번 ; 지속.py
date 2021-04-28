# https://www.acmicpc.net/problem/11648

# 첫 번째 줄에는 선행하는 0이 없는 9자리 이하의 수를 하나 입력합니다.
num = input()

# 기쁨이 지속될 수 있는 단계의 수를 저장하는 변수를 선언합니다.
happy_phase = 0

# 각 단계의 곱셈의 결과를 잠시 저장하는 변수를 선언합니다.
multiple = 1

# 각 자리 숫자를 모두 곱해서 하나의 수를 만든 후, 한 자리 숫자가 나올 때까지 반복합니다.
while True:
    # 곱셈의 결과가 한 자리 숫자라면
    if len(str(num)) == 1:
        # 기쁨이 지속될 수 있는 단계의 수를 출력합니다.
        print(happy_phase)
        # 반복문을 탈출합니다.
        break

    # 숫자의 한 자리씩 반복합니다.
    for digit in num:
        # multiple에 숫자 하나씩 곱합니다.
        multiple *= int(digit)

    # 기쁨이 지속될 수 있는 단계에 1을 추가합니다.
    happy_phase += 1
    # 곱셈의 결과를 num 변수에 문자열 형태로 저장합니다.
    num = str(multiple)
    # 잠시 저장하는 multiple은 1로 다시 초기화 해줍니다.
    multiple = 1