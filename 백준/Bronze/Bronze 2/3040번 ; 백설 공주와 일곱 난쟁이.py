# https://www.acmicpc.net/problem/3040

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 아홉 난쟁이들의 값들을 저장할 리스트 변수를 선언합니다.
nine_dwarfs = [None] * 9

# 9번 반복합니다.
for dwarf_idx in range(9):
    # 현재 인덱스 난쟁이의 값을 입력하고 리스트 변수에 넣어줍니다.
    # 값은 1보다 크거나 같고 99보다 작거나 같은 자연수입니다.
    # 정수형으로 변환합니다.
    nine_dwarfs[dwarf_idx] = int(stdin.readline())

# 아홉 난쟁이의 값들을 합한 값을 저장하는 변수를 선언합니다.
sum_nine_dwarfs = sum(nine_dwarfs)
# 합이 100이 되는 일곱 난장이의 수를 찾았는지 못 찾았는지를 저장하는 변수를 선언합니다.
find_seven = False

# 일곱 난쟁이의 값이 100이 될 때 이에 속하지 않는 두 난쟁이들을 찾는 반복문을 돌려봅니다.
for i in range(8):
    for j in range(i+1, 9):
        # 아홉 난쟁이 총합 값에서 현재 인덱스 두 난쟁이들의 값을 뺀 것을 저장하는 변수를 선언합니다.
        sum_seven_dwarfs = sum_nine_dwarfs - (nine_dwarfs[i] + nine_dwarfs[j])

        # 일곱 난쟁이들의 총합 값이 100인 경우
        if sum_seven_dwarfs == 100:
            # 필요없는 현재 두 인덱스 난쟁이들의 값을 False로 바꿔줍니다.
            nine_dwarfs[i] = False
            nine_dwarfs[j] = False
            # 합이 100이 되는 일곱 난쟁이를 찾았으므로 find_seven의 값을 True로 변경합니다.
            find_seven = True
            # 합이 100이 되는 일곱 난쟁이를 찾았으므로 반복문을 탈출합니다.
            break

    # 합이 100이 되는 일곱 난쟁이를 찾았으므로 반복문을 탈출합니다.
    if find_seven:
        break

# 아홉 난쟁이들의 값들 중 False인 값을 빼고 한 줄에 하나씩 출력합니다.
for dwarf in nine_dwarfs:
    if dwarf:
        print(dwarf)