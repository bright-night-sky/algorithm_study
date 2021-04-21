# https://www.acmicpc.net/problem/12778

# 첫 줄에는 시험문제의 개수 T를 입력합니다.
# 1 <= T <= 50
T = int(input())

# 시험문제의 개수 T만큼 반복합니다.
for question in range(T):
    # 알파벳 또는 숫자의 개수 M과 문제의 종류를 나타내는 문자를 입력합니다.
    # 1 <= M <= 500
    # 알파벳을 숫자로 바꾸는 문제인 경우에는 C, 숫자를 문자로 바꾸는 문제인 경우에는 N을 입력합니다.
    M, question_type = input().split(' ')
    # 문제의 종류에 따라 공백으로 구분해 알파벳(A~Z, 대문자) 또는 숫자(1~26, 정수)를 M개 입력합니다.
    num_or_alphabet = input().split(' ')

    # 정답을 저장하는 리스트 변수를 선언합니다.
    solutions = []

    # 문제의 종류가 알파벳을 숫자로 바꾸는 문제인 C인 경우
    if question_type == 'C':
        # 문제를 한 알파벳씩 반복합니다.
        for alphabet in num_or_alphabet:
            # 현재 알파벳을 숫자로 바꿔 저장하는 변수입니다.
            solution = ord(alphabet) - 64
            # 알파벳을 숫자로 바꾼 변수의 값을 정답을 저장하는 리스트 변수에 넣어줍니다.
            solutions.append(str(solution))
    # 문제의 종류가 숫자를 알파벳으로 바꾸는 문제인 N인 경우
    else:
        # 문제를 한 숫자씩 반복합니다.
        for number in num_or_alphabet:
            # 현재 숫자를 알파벳으로 바꿔 저장하는 변수입니다.
            solution = chr(int(number) + 64)
            # 숫자를 알파벳으로 바꾼 변수의 값을 정답을 저장하는 리스트 변수에 넣어줍니다.
            solutions.append(solution)

    # 정답 리스트 변수의 값들을 공백으로 구분해 출력합니다.
    print(' '.join(solutions))