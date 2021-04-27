# https://www.acmicpc.net/problem/2562

# 입력받은 자연수들을 차례대로 저장할 리스트 변수를 선언합니다.
numbers = []

# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수를 입력합니다.
for i in range(9):
    # 자연수 하나를 입력합니다.
    num = int(input())

    # 입력받은 자연수를 numbers 리스트 변수에 넣어줍니다.
    numbers.append(num)

# numbers 리스트 변수에서 가장 큰 값을 저장하는 변수를 선언합니다.
max_num = max(numbers)

# numbers 리스트 변수에서 가장 큰 값의 순서를 저장하는 변수를 선언합니다.
# 문제에서는 순서를 1부터 세므로 1을 더해줍니다.
max_num_index = numbers.index(max_num) + 1

# 출력 형식에 맞게 최댓값과 최댓값의 순서를 출력합니다.
print(max_num)
print(max_num_index)