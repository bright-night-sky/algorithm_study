# https://www.acmicpc.net/problem/3047

# 첫째 줄에 세 수 A, B, C를 입력합니다.
# 순서는 A, B, C가 아닐 수도 있습니다.
# 세 수는 100보다 작거나 같은 자연수입니다.
numbers = list(map(int, input().split(' ')))

# 둘째 줄에는 A, B, C로 이루어진 세 글자를 입력합니다.
ABC = input()

# numbers에서 최댓값을 저장하는 변수를 선언합니다.
max_num = max(numbers)
# numbers에서 최솟값을 저장하는 변수를 선언합니다.
min_num = min(numbers)

# numbers에서 최댓값과 최솟값을 삭제해줍니다.
numbers.remove(max_num)
numbers.remove(min_num)

# ABC에서 한 글자씩 반복해봅니다.
for alphabet in ABC:
    # 현재 알파벳이 A라면
    if alphabet == 'A':
        # 최솟값을 출력합니다.
        # 출력 형식에 맞게 한 칸 띄어줍니다.
        print(min_num, end=' ')
    # 현재 알파벳이 C라면
    elif alphabet == 'C':
        # 최댓값을 출력합니다.
        # 출력 형식에 맞게 한 칸 띄어줍니다.
        print(max_num, end=' ')
    # 현재 알파벳이 B라면
    else:
        # numbers에서 남은 값을 출력합니다.
        # 출력 형식에 맞게 한 칸 띄어줍니다.
        print(numbers[0], end=' ')