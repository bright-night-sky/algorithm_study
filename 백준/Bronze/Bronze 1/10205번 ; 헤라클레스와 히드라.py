# https://www.acmicpc.net/problem/10205

# 첫 번째 줄에는 data set의 개수 K를 입력합니다.
K = int(input())

# data set의 개수만큼 반복해봅니다.
for data_set_num in range(K):
    # 히드라의 머리 개수를 입력합니다.
    # 1 이상 50 이하입니다.
    hydra_heads = int(input())
    # 헤라클레스와 이올라우스의 일련의 행동들을 입력합니다.
    # 100글자 이하의 문자열입니다.
    actions = input()

    # 헤라클레스와 이올라우스의 행동들 문자열을 한 글자씩 반복합니다.
    for action in actions:
        # 현재 글자가 c라면
        if action == 'c':
            # 히드라의 머리가 하나 늘어나므로 1을 추가해줍니다.
            hydra_heads += 1
        # 현재 글자가 b라면
        else:
            # 히드라의 머리가 하나 줄어들므로 1을 빼줍니다.
            hydra_heads -= 1

        # 행동을 하고 난 후 히드라의 머리가 0개라면
        if hydra_heads == 0:
            # 반복문을 탈출합니다.
            break

    # 출력 형식에 맞게 출력합니다.
    print(f"Data Set {data_set_num+1}:")
    print(hydra_heads)
    print()