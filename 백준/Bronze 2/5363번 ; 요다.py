# https://www.acmicpc.net/problem/5363

# 첫째 줄에 문장의 수 N을 입력합니다.
N = int(input())

# 문장의 수만큼 반복합니다.
for i in range(N):
    # 한 문장을 입력합니다.
    # 문장의 길이는 100글자 이하입니다.
    # 한 문장에서 단어의 개수는 3개 이상입니다.
    # 입력한 문자를 공백으로 구분해서 한 단어씩 리스트 변수에 넣어서 저장합니다.
    sentence = input().split(' ')

    # 입력한 문장에서 앞의 두 단어를 떼서 맨 뒤에 붙인 결과를 변수에 저장합니다.
    result = sentence[2:] + sentence[0:2]

    # 리스트 변수의 값들을 중간에 공백을 넣어 문자열 형식으로 출력합니다.
    print(' '.join(result))