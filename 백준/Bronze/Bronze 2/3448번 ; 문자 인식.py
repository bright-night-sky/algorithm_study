# https://www.acmicpc.net/problem/3448

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에는 테스트 케이스의 개수 N을 입력합니다.
N = int(stdin.readline())

# 테스트 케이스의 개수 N만큼 반복합니다.
for test_case_idx in range(N):
    # 한 테스트 케이스에서의 모든 문장을 저장하는 변수를 선언합니다.
    all_sentence = ''

    # 한 테스트 케이스에서 모든 문장을 반복해봅니다.
    for line in stdin:
        # 각 테스트 케이스의 다음 줄에는 빈 줄이 한 칸씩 있으므로
        # 현재 한 줄이 다음 줄로 넘어가는 빈 문장이라면
        if line == '\n':
            # all_sentence의 맨 오른쪽의 \n을 지워줍니다.
            all_sentence = all_sentence.rstrip('\n')
            # 반복문을 탈출합니다.
            break
        # 현재 한 줄에 글씨들이 있다면
        else:
            # 현재 한 줄의 맨 오른쪽의 \n을 지우고 all_sentence에 넣어줍니다.
            all_sentence += line.rstrip('\n')

    # 전체 문자의 수를 저장하는 변수를 선언합니다.
    A = len(all_sentence)
    # 전체 문자에서 #을 뺀 인식한 문자의 수를 저장하는 변수를 선언합니다.
    R = A - all_sentence.count('#')
    # 인식률을 저장하는 변수를 선언합니다.
    # 소수점 둘째 자리에서 반올림합니다.
    R_divide_A = round(R / A * 100, 1)

    # R_divide_A의 소수 부분이 0이라면
    if str(R_divide_A).split('.')[-1] == '0':
        # 정수형으로 변환해줍니다.
        R_divide_A = int(R_divide_A)

    # 출력 형식에 맞게 출력합니다.
    print(f"Efficiency ratio is {R_divide_A}%.")