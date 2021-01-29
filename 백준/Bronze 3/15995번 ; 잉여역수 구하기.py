# https://www.acmicpc.net/problem/15995

# 첫째 줄에 서로소인 두 자연수 a와 m을 공백을 두고 입력합니다.
# 2 <= a, m <= 10,000
a, m = map(int, input().split(' '))

# 잉여역수 a*을 저장하는 변수입니다.
a_star = 1

# a_star을 1씩 증가시켜 보면서 잉여역수를 찾아봅니다.
while True:
    # a_star의 값이 잉여역수에 대한 조건을 만족한다면,
    if (a * a_star) % m == 1:
        # a_star가 최소의 잉여역수이므로 출력합니다.
        print(a_star)
        # 찾았으므로 반복문을 탈출합니다.
        break
    # a_star의 값이 잉여역수에 대한 조건을 만족하지 못한다면,
    else:
        # a_star을 1 증가시킵니다.
        a_star += 1