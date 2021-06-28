# https://www.acmicpc.net/problem/1972

# readline을 사용하기 위해 import합니다.
from sys import stdin


# *을 입력할 때까지 반복합니다.
while True:
    # 문자열을 입력합니다.
    # 대문자 알파벳으로만 이루어져 있거나, * 하나만 입력합니다.
    # 길이는 80을 넘지 않습니다.
    # 맨 끝의 \n은 떼어줍니다.
    string = stdin.readline().rstrip()

    # *을 입력했다면
    if string == '*':
        # 반복문을 탈출합니다.
        break

    # 입력한 문자열의 길이를 저장하는 변수를 선언합니다.
    N = len(string)
    # 입력한 문자열이 놀라운 문자열인지 아닌지를 저장하는 변수를 선언합니다.
    # 처음에는 놀라운 문자열이라는 뜻의 surprising으로 초기화합니다.
    is_surprising = 'surprising'

    # D-쌍을 뜻하는 D를 1부터 N-1까지 반복합니다.
    for D in range(1, N):
        # 현재 D에서의 D-쌍들을 저장할 리스트 변수를 선언합니다.
        D_pairs = []

        # 입력한 문자열의 인덱스를 0부터 N-D-1까지 반복합니다.
        for idx in range(0, N-D):
            # 문자열의 현재 인덱스에서 현재 D에서의 D-쌍을 저장하는 변수를 선언합니다.
            D_pair = string[idx] + string[idx+D]

            # D_pair가 D_pairs에 이미 있다면
            if D_pair in D_pairs:
                # 현재 D-쌍에서 유일하지 않으므로 놀라운 문자열이 아닙니다.
                # is_surprising에 NOT surprising을 저장합니다.
                is_surprising = 'NOT surprising'
                # 놀라운 문자열이 아닌 것이 확정되었으므로 반복문을 탈출합니다.
                break
            # D_pair가 D_pairs에 없다면
            else:
                # D_pairs에 D_pair를 넣어줍니다.
                D_pairs.append(D_pair)

        # is_surprising의 값이 NOT surprising이라면
        if is_surprising == 'NOT surprising':
            # 놀라운 문자열이 아닌 것이 확정되었으므로 반복문을 탈출합니다.
            break

    # 문자열이 놀라운 문자열인지 아닌지를 출력 형식에 맞게 출력합니다.
    print(f'{string} is {is_surprising}.')