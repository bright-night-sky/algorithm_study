# https://www.acmicpc.net/problem/13420

# 첫 번째 줄에는 테스트 케이스의 개수 T를 입력합니다.
T = int(input())

# 테스트 케이스의 개수 T만큼 반복해봅니다.
for test_case_index in range(T):
    # 수식을 하나 입력합니다.
    # 공백으로 구분해 리스트 변수로 반환합니다.
    equation = input().split(' ')

    # 수식의 첫 번째 수를 저장하는 변수를 선언합니다.
    num1 = int(equation[0])
    # 수식의 두 번째 수를 저장하는 변수를 선언합니다.
    num2 = int(equation[2])
    # 수식의 연산자를 저장하는 변수를 선언합니다.
    operator = equation[1]
    # 수식의 정답 부분을 저장하는 변수를 선언합니다.
    answer = int(equation[4])

    # 수식의 연산자가 +일 때
    if operator == '+':
        # num1과 num2의 합한 결과가 수식의 정답과 같다면
        if num1 + num2 == answer:
            print("correct")
        # num1과 num2의 합한 결과가 수식의 정답과 다르다면
        else:
            # wrong answer를 출력합니다.
            print("wrong answer")
    # 수식의 연산자가 -일 때
    elif operator == '-':
        # num1과 num2의 뺀 결과가 수식의 정답과 같다면
        if num1 - num2 == answer:
            # correct를 출력합니다.
            print("correct")
        # num1과 num2의 뺀 결과가 수식의 정답과 다르다면
        else:
            # wrong answer를 출력합니다.
            print("wrong answer")
    # 수식의 연산자가 *일 때
    elif operator == '*':
        # num1과 num2의 곱한 결과가 수식의 정답과 같다면
        if num1 * num2 == answer:
            # correct를 출력합니다.
            print("correct")
        # num1과 num2의 곱한 결과가 수식의 정답과 다르다면
        else:
            # wrong answer를 출력합니다.
            print("wrong answer")
    # 수식의 연산자가 /일 때
    else:
        # num1과 num2의 나눈 결과가 수식의 정답과 같다면
        if int(num1 / num2) == answer:
            # correct를 출력합니다.
            print("correct")
        # num1과 num2의 나눈 결과가 수식의 정답과 다르다면
        else:
            # wrong answer를 출력합니다.
            print("wrong answer")