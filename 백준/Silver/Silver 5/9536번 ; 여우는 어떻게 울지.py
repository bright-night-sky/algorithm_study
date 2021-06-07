# https://www.acmicpc.net/problem/9536

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫 번째 줄에는 테스트 케이스의 개수 T를 입력합니다.
# 정수형으로 변환합니다.
T = int(stdin.readline())

# 테스트 케이스의 개수 T만큼 반복합니다.
for test_case_idx in range(T):
    # 몇 개의 단어로 이루어진 녹음된 소리를 입력합니다.
    # 맨 끝의 \n은 제거하고 공백을 기준으로 분리합니다.
    record = stdin.readline().rstrip().split(' ')
    # 여우 외의 다른 동물들의 울음소리를 저장할 리스트 변수를 저장합니다.
    animal_cries = []
    # 여우의 울음소리를 저장할 변수를 선언합니다.
    result = ''

    # what does the fox say?를 입력할 때까지 반복합니다.
    while True:
        # 동물의 울음소리를 입력합니다.
        # 맨 끝의 \n은 제거합니다.
        animal_cry = stdin.readline().rstrip()

        # 입력한 동물의 울음소리가 what does the fox say?라면
        if animal_cry == "what does the fox say?":
            # 반복문을 탈출합니다.
            break

        # 입력한 동물의 울음소리를 저장하는 변수를 선언합니다.
        animal_cry = animal_cry.split(' ')[2]
        # animal_cry를 animal_cries에 넣어줍니다.
        animal_cries.append(animal_cry)

    # 녹음된 소리를 한 울음소리 단어씩 반복합니다.
    for cry in record:
        # 현재 울음소리 단어가 animal_cries에 속하지 않는다면
        if cry not in animal_cries:
            # result에 현재 울음소리 단어와 공백을 넣어줍니다.
            result += cry + ' '

    # 최종적인 여우 울음소리를 출력합니다.
    print(result)