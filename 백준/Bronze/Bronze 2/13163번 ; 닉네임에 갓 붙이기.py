# https://www.acmicpc.net/problem/13163

# 첫 번째 줄에는 닉네임의 수 N을 입력합니다.
# 1 <= N <= 100
N = int(input())

# 닉네임의 수 N만큼 반복합니다.
for i in range(N):
    # 음절 단위로 쪼갠 닉네임을 입력합니다.
    # 공백을 기준으로 나눈 값들을 변수 split_nickname에 저장합니다.
    split_nickname = input().split(' ')

    # 입력할 때 애초에 음절 단위로 쪼개어서 입력을 해줬으므로
    # "".join(split_nickname[1:])을 통해
    # 리스트 형태인 split_nickname에서
    # 첫 번째 음절인 0번째 인덱스의 값을을 빼고
    # 나머지 뒷부분을 공백없이 이어붙여서 문자열을 만들어줍니다.
    # 그 앞에 god을 붙인 문자열을 god_nickname 변수에 저장합니다.
    god_nickname = "god" + "".join(split_nickname[1:])

    # god_nickname의 값을 출력합니다.
    print(god_nickname)