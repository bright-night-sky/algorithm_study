# https://www.acmicpc.net/problem/4470

# 첫째 줄에 줄의 수 N을 입력합니다.
N = int(input())

# 줄의 수만큼 반복합니다.
for sentence_num in range(N):
    # 줄의 내용을 입력합니다.
    # 각 줄의 글자의 개수는 50글자를 넘지 않습니다.
    sentence = input()

    # 줄번호. 줄내용 형식으로 출력합니다.
    print(f"{sentence_num+1}. {sentence}")
