# https://www.acmicpc.net/problem/5426

# 제곱근 함수 sqrt를 쓰기 위해 import합니다.
from math import sqrt

# 첫째 줄에 테스트 케이스의 개수를 입력합니다.
# 테스트 케이스의 수는 최대 100개입니다.
test_case = int(input())

# 테스트 케이스의 개수만큼 반복합니다.
for i in range(test_case):
    # 암호화된 편지를 입력합니다.
    # 편지는 알파벳 소문자, 대문자로만 이루어져 있고,
    # 길이는 1보다 크거나 같고, 10,000보다 작거나 같으며, 항상 제곱수입니다.
    crypted_message = input()

    # 암호화된 편지의 길이의 제곱근을 저장하는 변수를 선언합니다.
    square_num = int(sqrt(len(crypted_message)))

    # 원래 메시지를 저장할 변수를 선언합니다.
    decrypted_message = ''

    # 암호화된 편지의 길이의 제곱근만큼 암호화된 편지를 나누어 본다고 생각합니다.
    # 그만큼 나누어진 각 단어에서 끝 글자부터 첫 글자까지 단어를 반복하면서 출력하면
    # 원래 메시지가 나옵니다.

    # 단어로 나누었을 때 끝 글자부터 첫 글자까지 반복해봅니다.
    for j in range(square_num-1, -1, -1):
        # 암호화된 편지를 길이의 제곱근 길이로 나누어 반복해봅니다.
        for index in range(0, len(crypted_message), square_num):
            # 암호화된 편지를 길이의 제곱근 길이로 나눈 단어를 저장하는 변수를 선언합니다.
            unit_word = crypted_message[index:index+square_num]

            # 나눈 단어에서 현재 반복 중인 위치의 글자를 원래 메시지 변수에 넣어줍니다.
            decrypted_message += unit_word[j]

    # 원래 메시지를 출력합니다.
    print(decrypted_message)