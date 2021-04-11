# https://www.acmicpc.net/problem/10102

# 첫째 줄에는 심사위원의 수 V를 입력합니다.
# 1 <= V <= 15
V = input()

# 둘째 줄에는 각 심사위원이 누구에게 투표했는지를 입력합니다.
vote_result = input()

# 심사위원의 투표에서 A의 개수를 저장하는 변수를 선언합니다.
A_num = vote_result.count('A')
# 심사위원의 투표에서 B의 개수를 저장하는 변수를 선언합니다.
B_num = vote_result.count('B')

# A의 개수가 B의 개수보다 많다면
if A_num > B_num:
    # A를 출력합니다.
    print('A')
# B의 개수가 A의 개수보다 많다면
elif A_num < B_num:
    # B를 출력합니다.
    print('B')
# A와 B의 개수가 같다면
else:
    # Tie를 출력합니다.
    print('Tie')