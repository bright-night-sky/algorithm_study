# https://www.acmicpc.net/problem/9046

# 첫 줄에는 테스트 케이스의 개수 T를 입력합니다.
# 1 <= T <= 20
T = int(input())

# 테스트 케이스의 개수만큼 반복합니다.
for i in range(T):
    # 소문자와 공백으로 이루어진 영어 문장을 입력합니다.
    # 길이는 1 이상 255 이하입니다.
    sentence = input()

    # 문장에서 가장 빈번하게 나타나는 소문자를 저장할 변수를 선언합니다.
    max_alphabet = ''
    # 문장에서 가장 빈번하게 나타나는 소문자의 빈도수를 저장할 변수를 선언합니다.
    max_alphabet_count = 0

    # 문장에서 소문자 a부터 z까지 반복하면서 빈도수를 체크해봅니다.
    for j in range(ord('a'), ord('z')+1):
        # 문장에서 현재 소문자의 빈도수를 저장하는 변수를 선언합니다.
        current_alphabet_count = sentence.count(chr(j))

        # 만약 현재 소문자의 빈도수가 이전까지 소문자에서의 최대 빈도수보다 크다면
        if current_alphabet_count > max_alphabet_count:
            # 최대 빈도수 소문자 변수에 현재 소문자를 저장합니다.
            max_alphabet = chr(j)
            # 최대 빈도수 변수에 현재 소문자의 빈도수를 저장합니다.
            max_alphabet_count = current_alphabet_count
        # 만약 현재 소문자의 빈도수가 이전까지 소문자에서의 최대 빈도수와 같다면
        elif current_alphabet_count == max_alphabet_count:
            # 최대 빈도수 소문자 변수에 ?를 저장합니다.
            max_alphabet = '?'
        # 만약 현재 소문자의 빈도수가 이전까지 소문자에서의 최대 빈도수보다 작다면
        else:
            # 그냥 넘어갑니다.
            continue

    # 최대 빈도수를 가진 소문자를 출력합니다.
    print(max_alphabet)