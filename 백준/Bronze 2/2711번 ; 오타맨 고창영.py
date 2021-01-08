# https://www.acmicpc.net/problem/2711

# 테스트 케이스 개수 T 입력
# 1 <= T <= 1000
T = int(input())

# 각 테스트 케이스를 순회
for i in range(0, T):
    # 오타를 낸 위치, 창영이가 친 문자열 입력
    mis_index, string = input().split(' ')
    # 오타를 낸 위치를 문자열 인덱스 문법에 맞게 조정
    mis_index = int(mis_index) - 1

    # 오타를 낸 위치의 문자열을 기준으로 각각 앞뒤로 자른 문자열을 저장
    pre_str = string[0:mis_index]
    suf_str = string[mis_index+1:]

    # 그 앞뒤 문자열 두 개를 합친 것이 오타를 지운 문자열이다.
    string = pre_str + suf_str

    # 오타를 지운 문자열 출력
    print(string)
