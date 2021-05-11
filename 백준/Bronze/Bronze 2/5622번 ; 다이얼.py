# https://www.acmicpc.net/problem/5622

# 첫째 줄에 알파벳 대문자로 이루어진 단어를 입력합니다.
# 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같습니다.
word = input()

# 다이얼을 걸기 위해서 필요한 최소 시간을 저장하는 변수를 선언합니다.
min_time = 0

# 입력한 단어에서 한 알파벳씩 반복합니다.
for alphabet in word:
    # 현재 알파벳이 A, B, C 중 하나라면
    if alphabet in 'ABC':
        # 최소 시간에 3초를 더해줍니다.
        min_time += 3
    # 현재 알파벳이 D, E, F 중 하나라면
    elif alphabet in 'DEF':
        # 최소 시간에 4초를 더해줍니다.
        min_time += 4
    # 현재 알파벳이 G, H, I 중 하나라면
    elif alphabet in 'GHI':
        # 최소 시간에 5초를 더해줍니다.
        min_time += 5
    # 현재 알파벳이 J, K, L 중 하나라면
    elif alphabet in 'JKL':
        # 최소 시간에 6초를 더해줍니다.
        min_time += 6
    # 현재 알파벳이 M, N, O 중 하나라면
    elif alphabet in 'MNO':
        # 최소 시간에 7초를 더해줍니다.
        min_time += 7
    # 현재 알파벳이 P, Q, R, S 중 하나라면
    elif alphabet in 'PQRS':
        # 최소 시간에 8초를 더해줍니다.
        min_time += 8
    # 현재 알파벳이 T, U, V 중 하나라면
    elif alphabet in 'TUV':
        # 최소 시간에 9초를 더해줍니다.
        min_time += 9
    # 현재 알파벳이 나머지 알파벳인 W, X, Y, Z 중 하나라면
    else:
        # 최소 시간에 10초를 더해줍니다.
        min_time += 10

# 다이얼을 걸기 위해서 필요한 최소 시간을 출력합니다.
print(min_time)