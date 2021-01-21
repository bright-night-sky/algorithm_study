# https://www.acmicpc.net/problem/2684

# 첫째 줄에 테스트 케이스의 개수 P 입력
# 1 <= P <= 1000
P = int(input())

# 각 3-동전수열을 저장한 리스트 변수
three_coin = ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH']

# 테스트 케이스 반복
for i in range(0, P):
    # 동전을 40번 던진 결과를 입력
    # 앞면은 H, 뒷면은 T
    case = input()

    # 각각의 3-동전수열의 경우를 세어본다.
    for coin in three_coin:
        # 현재 3-동전수열의 개수를 저장할 변수
        count = 0
        # 이번에 입력된 케이스에서 문자 3개씩 잘라서 비교해본다.
        for idx in range(0, 38):
            # 현재의 3-동전수열과 일치한다면
            if coin == case[idx:idx+3]:
                # 개수 1개 추가
                count += 1
        # 현재 3-동전수열의 개수를 출력하고 한 칸 띄운다.
        print(count, end=' ')

    # 한 케이스 출력이 끝나면 한 줄 밑으로 내린다.
    print()
