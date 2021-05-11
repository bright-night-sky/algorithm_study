# https://www.acmicpc.net/problem/1434

# 첫째 줄에 박스의 개수 N, 책의 개수 M을 입력합니다.
# 1 <= N, M <= 50
N, M = map(int, input().split(' '))

# 둘째 줄에는 박스의 용량 A1, A2, ..., AN을 입력합니다.
# 1 <= Ai <= 1,000
# 박스의 용량들을 A라는 리스트로 만들어줍니다.
A = [int(i) for i in input().split(' ')]

# 셋째 줄에는 책의 크기 B1, B2, ..., BM을 입력합니다.
# 1 <= Bj <= 1,000
# 책의 크기들을 B라는 리스트로 만들어줍니다.
B = [int(j) for j in input().split(' ')]

# 전체 박스의 낭비된 용량의 합을 저장하는 변수 waste를 만들어줍니다.
waste = []

for book in B:
    for box in A:
        # 현재 책이 현재 박스에 들어가지 않으면,
        if box < book:
            waste.push(box)
            A.remove(box)
        # 현재 책이 현재 박스에 들어갈 수 있으면,
        else:
            # 박스의 남은 용량은 낭비된 용량의 변수 waste에 더해줍니다.
            waste.push(box - book)
            # 현재 책을 박스에 담았으므로 반복문을 탈출
            A.remove(box)