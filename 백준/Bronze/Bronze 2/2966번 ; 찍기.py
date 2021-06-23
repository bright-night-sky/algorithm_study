# https://www.acmicpc.net/problem/2966

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 필기시험의 문제 수 N을 입력합니다.
# 1 <= N <= 100
# 정수형으로 변환합니다.
N = int(stdin.readline())
# 둘째 줄에 시험의 정답을 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
answer = stdin.readline().rstrip()
# 상근이의 찍기 패턴을 저장하는 리스트 변수를 선언합니다.
sang_pattern = ['A', 'B', 'C']
# 창영이의 찍기 패턴을 저장하는 리스트 변수를 선언합니다.
chang_pattern = ['B', 'A', 'B', 'C']
# 현진이의 찍기 패턴을 저장하는 리스트 변수를 선언합니다.
hyun_pattern = ['C','C', 'A', 'A', 'B', 'B']
# 상근이가 맞은 문제의 수를 저장하는 변수를 선언합니다.
sang_correct = 0
# 창영이가 맞은 문제의 수를 저장하는 변수를 선언합니다.
chang_correct = 0
# 현진이가 맞은 문제의 수를 저장하는 변수를 선언합니다.
hyun_correct = 0

# 문제의 수 N만큼 반복합니다.
for idx in range(N):
    # 현재 문제의 정답과 상근이의 찍기 패턴이 일치한다면
    if answer[idx] == sang_pattern[idx % 3]:
        # 상근이가 맞은 문제의 수에 1을 더합니다.
        sang_correct += 1

    # 현재 문제의 정답과 창영이의 찍기 패턴이 일치한다면
    if answer[idx] == chang_pattern[idx % 4]:
        # 창영이가 맞은 문제의 수에 1을 더합니다.
        chang_correct += 1

    # 현재 문제의 정답과 현진이의 찍기 패턴이 일치한다면
    if answer[idx] == hyun_pattern[idx % 6]:
        # 현진이가 맞은 문제의 수에 1을 더합니다.
        hyun_correct += 1

# 세 명의 맞은 문제의 수에서 가장 많은 정답의 수를 저장하는 변수를 선언합니다.
max_correct = max(sang_correct, chang_correct, hyun_correct)

# 가장 많은 정답의 수를 출력합니다.
print(max_correct)
# 가장 많은 정답의 수와 상근이의 정답의 수가 일치하면
if max_correct == sang_correct:
    # Adrian을 출력합니다.
    print('Adrian')
# 가장 많은 정답의 수와 창영이의 정답의 수가 일치하면
if max_correct == chang_correct:
    # Bruno를 출력합니다.
    print('Bruno')
# 가장 많은 정답의 수와 현진이의 정답의 수가 일치하면
if max_correct == hyun_correct:
    # Goran을 출력합니다.
    print('Goran')


