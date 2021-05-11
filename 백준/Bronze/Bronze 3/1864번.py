# https://www.acmicpc.net/problem/1864

# 문제에 나온 각각의 기호와 그에 대응하는 숫자를 dictionary로 만듦
char_num = {
    '-': 0,
    '\\': 1,
    '(': 2,
    '@': 3,
    '?': 4,
    '>': 5,
    '&': 6,
    '%': 7,
    '/': -1
}

# 한 줄에 하나씩 문어 숫자가 입력
# #이 입력될 때까지 계속 입력받는다.
while True:
    # 문어 숫자 입력
    string = input()

    # 입력 받은 문자가 #이면 입력 종료
    if string == '#':
        break

    # sum은 한 줄마다의 결과
    sum = 0

    for idx, char in enumerate(string):
        # exponent : 각 자리 숫자의 8의 지수
        exponent = len(string) - 1 - idx
        # 문어 숫자의 한 문자마다 계산해서 더함
        sum = sum + (char_num[char] * 8 ** exponent)

    # 한 줄마다의 문어 숫자 결과를 출력
    print(sum)