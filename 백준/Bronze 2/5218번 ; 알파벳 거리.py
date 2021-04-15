# https://www.acmicpc.net/problem/5218

# 첫째 줄에 테스트 케이스의 수를 입력합니다.
# 테스트 케이스의 수는 100보다 작습니다.
test_case = int(input())

# 테스트 케이스의 수만큼 반복합니다.
for i in range(test_case):
    # 길이가 같은 두 단어를 공백으로 구분해 입력합니다.
    # 단어의 길이는 4보다 크거나 같고, 20보다 작거나 같습니다.
    # 대문자로만 이루어져 있습니다.
    word1, word2 = input().split(' ')

    # 두 단어의 알파벳마다의 알파벳 거리들의 결과를 저장할 변수를 선언합니다.
    distance_result = ''

    # 두 단어에서 한 알파벳씩 반복해봅니다.
    for index in range(len(word1)):
        # word1에서 한 알파벳의 숫자를 계산해서 저장하는 변수를 선언합니다.
        x = ord(word1[index]) - 64
        # word2에서 한 알파벳의 숫자를 계산해서 저장하는 변수를 선언합니다.
        y = ord(word2[index]) - 64

        # 문제에서 y >= x의 조건을 만족하면
        if x <= y:
            # y - x의 값을 구해서 결과 변수에 저장합니다.
            distance_result += str(y - x) + " "
        # 문제에서 y < x의 조건을 만족하면
        else:
            # (y+26) - x의 값을 구해서 결과 변수에 저장합니다.
            distance_result += str(y + 26 - x) + " "

    # 이번 테스트 케이스에서의 결과를 출력합니다.
    print(f"Distances: {distance_result}")