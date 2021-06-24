# https://www.acmicpc.net/problem/21866

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 번째 줄에 각 문제에 대한 점수인 9개의 정수를 공백으로 구분해 입력합니다.
# 각 정수는 0 이상 1,000 이하의 정수입니다.
# 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
scores = list(map(int, stdin.readline().split(' ')))
# 각 문제 당 최대 점수를 저장하는 리스트 변수를 선언합니다.
max_scores = [100, 100, 200, 200, 300, 300, 400, 400, 500]
# 참가자가 해커인지의 여부를 저장할 변수를 선언합니다.
# False로 초기화합니다.
is_hacker = False

# 문제 개수인 9번만큼 반복합니다.
for idx in range(9):
    # 현재 문제에서 참가자가 얻은 점수가 최대로 얻을수 있는 점수보다 크다면
    if scores[idx] > max_scores[idx]:
        # 해커이므로 is_hacker에 True를 저장합니다.
        is_hacker = True
        # 참가자가 해커로 확정되었으므로 반복문을 탈출합니다.
        break

# 참가자가 해커라면
if is_hacker:
    # hacker를 출력합니다.
    print('hacker')
# 참가자의 총 점수가 100점보다 작다면
elif sum(scores) < 100:
    # none을 출력합니다.
    print('none')
# 그 외의 경우에는
else:
    # draw를 출력합니다.
    print('draw')