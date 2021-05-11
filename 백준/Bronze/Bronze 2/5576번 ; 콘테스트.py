# https://www.acmicpc.net/problem/5576

# W 대학의 각 참가자의 점수를 저장할 리스트 변수를 선언합니다.
W_university = []
# K 대학의 각 참가자의 점수를 저장할 리스트 변수를 선언합니다.
K_university = []

# 1~10행의 W 대학의 각 참가자의 점수를 입력합니다.
for i in range(10):
    # 1~10행의 W 대학의 각 참가자의 점수를 입력하고 리스트 변수에 넣습니다.
    W_university.append(int(input()))

# 11~20행의 K 대학의 각 참가자의 점수를 입력합니다.
for i in range(10):
    # 11~20행의 K 대학의 각 참가자의 점수를 입력하고 리스트 변수에 넣습니다.
    K_university.append(int(input()))

# W 대학 참가자들의 점수를 내림차순으로 정렬시키고,
# 득점이 높은 세 사람의 점수인 인덱스 0에서 2까지의 점수를 합쳐서 변수에 저장합니다.
W_top3 = sum(sorted(W_university, reverse=True)[0:3])
# K 대학 참가자들의 점수를 내림차순으로 정렬시키고,
# 득점이 높은 세 사람의 점수인 인덱스 0에서 2까지의 점수를 합쳐서 변수에 저장합니다.
K_top3 = sum(sorted(K_university, reverse=True)[0:3])

# W 대학 점수와 K 대학 점수를 공백으로 구분해 출력합니다.
print(W_top3, K_top3)
