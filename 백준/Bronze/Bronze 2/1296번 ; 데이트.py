# https://www.acmicpc.net/problem/1296

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 오민식의 영어 이름을 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
ohminsik = stdin.readline().rstrip()
# 둘째 줄에는 좋아하는 여자의 수 N을 입력합니다.
# 50보다 작거나 같은 자연수입니다.
# 정수형으로 변환합니다.
N = int(stdin.readline())
# 성공할 확률이 가장 높은 여자들의 이름들을 저장할 리스트 변수를 선언합니다.
selected_woman = []
# 성공할 확률 중 가장 높은 값을 저장할 변수를 선언합니다.
probability = 0

# 좋아하는 여자의 수 N만큼 반복합니다.
for woman_idx in range(N):
    # 여자의 이름을 입력합니다.
    # 알파벳 대문자로만 구성되어 있습니다.
    # 맨 끝의 \n은 떼어줍니다.
    woman_name = stdin.readline().rstrip()
    # 오민식 이름과 입력한 여자의 이름을 이은 변수를 선언합니다.
    name_sum = ohminsik + woman_name
    # 두 사람 이름에서 등장하는 L의 개수를 저장하는 변수를 선언합니다.
    L = name_sum.count('L')
    # 두 사람 이름에서 등장하는 O의 개수를 저장하는 변수를 선언합니다.
    O = name_sum.count('O')
    # 두 사람 이름에서 등장하는 V의 개수를 저장하는 변수를 선언합니다.
    V = name_sum.count('V')
    # 두 사람 이름에서 등장하는 E의 개수를 저장하는 변수를 선언합니다.
    E = name_sum.count('E')
    # 현재 여자와 성공할 확률을 계산한 값을 저장하는 변수를 선언합니다.
    woman_prob = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100

    # 이전까지의 가장 높은 확률과 현재 여자와 성공할 확률이 같다면
    if woman_prob == probability:
        # 성공할 확률이 가장 높은 여자들을 저장하는 리스트 변수에 현재 여자의 이름을 넣어줍니다.
        selected_woman.append(woman_name)
    # 이전까지의 가장 높은 확률보다 현재 여자와 성공할 확률이 크다면
    elif woman_prob > probability:
        # 성공할 확률이 가장 높은 여자들을 저장하는 리스트 변수들을 비워줍니다.
        selected_woman = list()
        # 성공할 확률이 가장 높은 여자들을 저장하는 리스트 변수에 현재 여자의 이름을 넣어줍니다.
        selected_woman.append(woman_name)
        # 성공할 확률 중 가장 높은 값을 저장하는 변수에 현재 여자와의 성공할 확률 값을 넣어줍니다.
        probability = woman_prob

# 성공할 확률이 가장 높은 여자의 이름 중 알파벳으로 가장 앞서는 이름을 출력합니다.
print(sorted(selected_woman)[0])