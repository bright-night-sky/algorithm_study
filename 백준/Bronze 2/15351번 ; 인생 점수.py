# https://www.acmicpc.net/problem/15351

# 첫 번째 줄에 즐기는 것의 개수 N을 입력합니다.
N = int(input())

# 즐기는 것의 개수 N만큼 반복합니다.
for i in range(N):
    # 즐기는 것을 입력합니다.
    # 영어 대문자와 띄어쓰기로 입력합니다.
    # 30자를 넘지 않습니다.
    enjoy = input()

    # 즐기는 것의 점수를 저장하는 변수를 선언합니다.
    score = 0

    # 즐기는 것의 한 글자씩 반복합니다.
    for alphabet in enjoy:
        # 현재 글자가 띄어쓰기라면
        if alphabet == " ":
            # 점수가 없으므로 그냥 넘어갑니다.
            continue
        # 현재 글자가 영어 대문자라면
        else:
            # 현재의 영어 대문자의 점수를 저장하는 변수를 선언합니다.
            alphabet_score = ord(alphabet) - 64
            # 영어 대문자의 점수를 즐기는 것의 점수에 더해줍니다.
            score += alphabet_score

    # 즐기는 것의 점수가 100이라면
    if score == 100:
        # PERFECT LIFE를 출력합니다.
        print("PERFECT LIFE")
    # 즐기는 것의 점수가 100 이외의 점수라면
    else:
        # 점수를 출력합니다.
        print(score)