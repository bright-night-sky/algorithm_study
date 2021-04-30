# https://www.acmicpc.net/problem/11536

# 첫째 줄에 이름의 개수 N을 입력합니다.
# 2 <= N <= 20
N = int(input())

# 선수들의 이름을 저장하는 리스트 변수를 선언합니다.
names = []

# 이름의 개수 N만큼 반복합니다.
for name_index in range(N):
    # 선수의 이름을 입력합니다.
    # 이름은 2 이상 12 이하의 대문자로만 이루어져 있습니다.
    # 선수의 이름은 중복되지 않습니다.
    name = input()

    # 선수의 이름을 names 리스트 변수에 넣어줍니다.
    names.append(name)

# names를 오름차순으로 정렬하고 저장한 리스트 변수를 선언합니다.
increase_names = sorted(names)
# names를 내림차순으로 정렬하고 저장한 리스트 변수를 선언합니다.
decrease_names = sorted(names, reverse=True)

# names가 오름차순으로 정렬된 리스트와 같다면
if names == increase_names:
    # INCREASING을 출력합니다.
    print("INCREASING")
# names가 내림차순으로 정렬된 리스트와 같다면
elif names == decrease_names:
    # DECREASING을 출력합니다.
    print("DECREASING")
# 어느 것도 같지 않다면
else:
    # NEITHER을 출력합니다.
    print("NEITHER")