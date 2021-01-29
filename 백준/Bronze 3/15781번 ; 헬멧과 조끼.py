# https://www.acmicpc.net/problem/15781

# 첫째 줄에 맵에 존재하는 헬멧의 개수 N, 조끼의 개수 M을 입력합니다.
# N : 1000 이하의 자연수
# M : 1000 이하의 자연수
N, M = map(int, input().split(' '))

# 둘째 줄에 각 헬멧의 방어력을 N개 만큼 입력합니다.
h = list(map(int, input().split(' ')))

# 셋째 줄에 각 조끼의 방어력을 M개 만큼 입력합니다.
a = list(map(int, input().split(' ')))

# 헬멧과 조끼에서 최대의 방어력을 뽑아내고 그 둘을 더하면 얻을 수 있는 방어력의 최댓값입니다.

# 헬멧에서 최대의 방어력을 저장하는 변수입니다.
helmet_max = max(h)

# 조끼에서 최대의 방어력을 저장하는 변수입니다.
armor_max = max(a)

# 얻을 수 있는 방어력의 최댓값을 출력합니다.
print(helmet_max + armor_max)