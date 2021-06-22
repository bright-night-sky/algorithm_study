# https://www.acmicpc.net/problem/2495

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 여덟 자리 양의 정수를 3개 입력하므로 3번 반복합니다.
for _ in range(3):
    # 여덟 자리 양의 정수를 입력합니다.
    # 맨 끝의 \n은 떼어줍니다.
    num = stdin.readline().rstrip()
    # 연속해서 나오는 구간 중 가장 긴 것의 길이를 저장할 변수를 선언합니다.
    # 최소 연속구간은 모두 연속하지 않는 경우이므로 1로 초기화합니다.
    max_same_num_cnt = 1

    # 현재 연속 중인 숫자를 저장하는 변수를 선언합니다.
    # 맨 처음 숫자로 초기화합니다.
    cur_num = num[0]
    # 현재 연속 중인 숫자의 연속 구간 길이를 저장할 변수를 선언합니다.
    # 최소 연속구간은 모두 연속하지 않는 경우이므로 1로 초기화합니다.
    cur_num_same_cnt = 1
    # 여덟 자리 양의 정수에서 두 번째 숫자부터 끝까지 반복합니다.
    for idx in range(1, 8):
        # 현재 숫자가 바로 뒤의 숫자와 같다면
        if num[idx] == num[idx - 1]:
            # 현재 연속 중인 숫자의 연속 구간 길이에 1을 더해줍니다.
            cur_num_same_cnt += 1

            # 현재 연속 중인 숫자의 연속 구간 길이의 값이 이전까지의 연속 구간 중 가장 긴 것의 길이의 값보다 크다면
            if cur_num_same_cnt > max_same_num_cnt:
                # 현재 연속 중인 숫자의 연속 구간 길이의 값을 연속해서 나오는 구간 중 가장 긴 것의 길이에 넣어줍니다.
                max_same_num_cnt = cur_num_same_cnt
        # 현재 숫자가 바로 뒤의 숫자와 다르다면
        else:
            # 현재 연속 중인 숫자 변수에 현재 숫자를 넣어줍니다.
            cur_num = num[idx]
            # 현재 연속 중인 숫자의 연속 구간 길이를 1로 만듭니다.
            cur_num_same_cnt = 1

    # 연속 구간 중 가장 긴 것의 길이를 출력합니다.
    print(max_same_num_cnt)