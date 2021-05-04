# https://www.acmicpc.net/problem/11728

# 첫째 줄에 배열 A의 크기 N, 배열 B의 크기 M을 입력합니다.
# 1 <= N, M <= 1,000,000
N, M = map(int, input().split(' '))

# 배열 A의 내용을 공백으로 구분해 입력합니다.
A = list(map(int, input().split(' ')))
# 배열 B의 내용을 공백으로 구분해 입력합니다.
B = list(map(int, input().split(' ')))
# 배열에 들어있는 수는 절댓값이 10^9보다 작거나 같은 정수입니다.

# 배열 A에 배열 B를 연결해줍니다.
A.extend(B)
# 배열 B가 연결된 배열 A를 오름차순으로 정렬합니다.
A.sort()

# 오름차순 된 배열 A를 출력 형식에 맞게 하나씩 출력합니다.
for number in A:
    print(number, end=' ')