# https://www.acmicpc.net/problem/3449

# 첫째 줄에는 테스트 케이스의 개수 T를 입력합니다
T = int(input())

# 테스트 케이스의 수만큼 반복문을 돌립니다.
for i in range(0, T):
    # 한 줄씩 이진수를 입력합니다.
    # 두 이진수는 길이가 같고, 100자리를 넘지 않습니다.
    bin1 = input()
    bin2 = input()

    # 해밍 거리를 저장하는 변수입니다.
    # 0으로 초기화해줍니다.
    hamming_distance = 0

    # 두 이진수의 길이만큼 각 자리수를 비교해봅니다.
    for idx in range(0, len(bin1)):
        # 만약 두 이진수의 현재 자리수가 다르다면,
        if bin1[idx] != bin2[idx]:
            # 해밍 거리에 1을 더해줍니다.
            hamming_distance += 1

    # 결과를 출력합니다.
    print(f"Hamming distance is {hamming_distance}.")