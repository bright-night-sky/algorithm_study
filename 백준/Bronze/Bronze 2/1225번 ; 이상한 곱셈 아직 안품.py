# https://www.acmicpc.net/problem/1225

# A, B 입력
# 두 수는 모두 10,000자리를 넘지 않는다.
A, B = input().split(' ')

# 곱셈 결과를 저장할 변수
sum = 0

# A 숫자를 한 자리씩 탐색
for i in A:
    # B 숫자를 한 자리씩 탐색
    for j in B:
        # A와 B의 각 자리 숫자를 곱한 것을 곱셈 결과에 더한다.
        sum += (int(i) * int(j))

# 곱셈 결과를 출력
print(sum)