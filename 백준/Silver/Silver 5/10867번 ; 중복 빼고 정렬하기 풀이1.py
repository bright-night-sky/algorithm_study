# https://www.acmicpc.net/problem/10867

# 첫째 줄에 수의 개수 N을 입력합니다.
# 1 <= N <= 100,000
N = int(input())

# 둘째 줄에 숫자들을 공백으로 구분해 입력합니다.
# 숫자들은 절댓값이 1,000 보다 작거나 같은 정수입니다.
numbers = list(map(int, input().split(' ')))

# 같은 수가 없는 숫자들을 저장하는 리스트 변수를 선언합니다.
not_overlap_numbers = []

# 입력한 숫자들을 하나씩 반복해봅니다.
for num in numbers:
    # 현재 숫자가 not_overlap_numbers 리스트 변수에 없다면
    if num not in not_overlap_numbers:
        # 현재 숫자를 not_overlap_numbers 리스트 변수에 넣어줍니다.
        not_overlap_numbers.append(num)

# not_overlap_numbers에 있는 숫자들을 오름차순으로 정렬해줍니다.
not_overlap_numbers.sort()
# not_overlap_numbers에 있는 숫자들을 문자열 형태로 바꿔서 저장합니다.
sorted_not_overlap_numbers = list(map(str, not_overlap_numbers))

# 숫자들을 공백으로 구분해 출력합니다.
print(' '.join(sorted_not_overlap_numbers))