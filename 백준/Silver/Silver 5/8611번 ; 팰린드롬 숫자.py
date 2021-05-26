# https://www.acmicpc.net/problem/8611

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 n을 입력합니다.
# 1 <= n <= 10^1000
# 정수형으로 변환합니다.
n = int(stdin.readline())
# 팰린드롬이 없는 상태를 저장하는 변수를 선언합니다.
# True로 초기화합니다.
no_palindrome = True

# 2부터 9진법까지 반복해봅니다.
for b in range(2, 10):
    # n의 값을 복사해 온 변수를 선언합니다.
    number = n
    # b진법으로 변환한 결과를 저장할 변수를 선언합니다.
    m = ''

    # number를 b진법으로 변환합니다.
    # number가 b보다 작아질 때까지 반복합니다.
    while number >= b:
        # m에는 number를 b로 나눈 나머지를 넣어줍니다.
        m += str(number % b)
        # number는 b로 나눈 몫으로 다시 초기화해줍니다.
        number //= b
    # 마지막으로 남은 number의 값도 m에 넣어줍니다.
    m += str(number)
    # m에 저장한 b진법으로 변환한 결과는 실제 b진법으로 변환한 결과가 뒤집어진 상태로 저장되어 있습니다.
    # 팰린드롬인지 아닌지 여부만 보면 되므로 한 번 더 뒤집어서 실제 b진법의 결과를 저장할 필요가 없습니다.

    # m과 m의 역순이 같다면
    if m == m[::-1]:
        # 팰린드롬이 있으므로 no_palindrome에 False를 저장합니다.
        no_palindrome = False
        # 출력 형식에 맞게 현재 진법과 그 진법에서의 결과를 공백을 두고 출력합니다.
        print(f'{b} {m}')

# 10진법일 때의 결과는 입력한 n을 그대로 검사하면 되므로 따로 빼줍니다.
# n과 n의 역순이 같다면
if str(n) == str(n)[::-1]:
    # 출력 형식에 맞게 10과 n을 공백을 두고 출력합니다.
    print(f'10 {n}')
# 이 때까지 팰린드롬이 없었다면 no_palindrome은 True이므로
elif no_palindrome:
    # NIE를 출력합니다.
    print('NIE')
