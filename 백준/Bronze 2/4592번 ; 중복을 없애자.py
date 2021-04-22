# https://www.acmicpc.net/problem/4592

# 0 하나를 입력할 때까지 반복합니다.
while True:
    # 0 혹은 공백으로 구분된 일련의 숫자들을 입력합니다.
    numbers = input()

    # 결과를 저장하는 변수를 선언합니다.
    result = ""

    # 입력값이 0 하나라면
    if numbers == "0":
        # 반복문을 탈출하고 종료합니다.
        break
    # 입력값이 공백으로 구분된 일련의 숫자라면
    else:
        # 숫자들을 공백으로 구분해 리스트 형태로 저장하는 변수를 선언합니다.
        numbers = numbers.split(' ')

        # 리스트 변수에서 맨 앞에 있는 숫자는 N입니다.
        # 0 <= N <= 25
        N = int(numbers[0])
        # 리스트 변수에서 그 이후에 있는 숫자들은 방문자들이 제출한 값들입니다.
        # 1부터 99 사이의 수입니다.
        numbers = numbers[1:]

        # 일단 결과 변수에는 방문자들이 제출한 값 중 맨 앞에 있는 값과 공백을 넣어줍니다.
        result += numbers[0] + " "

        # 방문자들이 제출한 숫자 중 두 번째부터 끝까지 반복해봅니다.
        for index in range(1, N):
            # 리스트 변수에서 현재 숫자가 바로 앞의 숫자와 똑같은 숫자가 아니라면
            if numbers[index-1] != numbers[index]:
                # 결과 변수에 현재 숫자와 공백을 넣어줍니다.
                result += numbers[index] + " "

        # 출력 형식에 맞게 결과 변수의 갑과 맨 뒤에 $를 같이 출력합니다.
        print(f"{result}$")