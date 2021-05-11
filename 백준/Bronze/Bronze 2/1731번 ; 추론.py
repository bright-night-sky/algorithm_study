# https://www.acmicpc.net/problem/1731

# 첫째 줄에 수열의 길이 N을 입력합니다.
# 항상 3 이상 50 이하입니다.
N = int(input())

# 입력하는 수열의 각 원소들을 저장하는 리스트 변수를 선언합니다.
numbers = []

# 등차수열인지 등비수열인지를 저장하는 변수를 선언합니다.
difference_or_ratio = None

# 수열의 길이 N만큼 반복합니다.
for index in range(N):
    # 수열의 원소 하나를 입력합니다.
    number = int(input())

    # 입력한 수열의 원소 하나를 numbers 리스트 변수에 넣어줍니다.
    numbers.append(number)

# 문제에서 주어지는 수열은 등차수열 혹은 등비수열 중 하나에만 속합니다.
# 수열의 세 번째 원소와 두 번째 원소와의 차이가
# 수열의 두 번째 원소와 첫 번째 원소와의 차이와 같다면
if numbers[2] - numbers[1] == numbers[1] - numbers[0]:
    # 등차수열이므로 difference_or_ratio 변수에 "difference"를 저장해줍니다.
    difference_or_ratio = "difference"
    # 공차 Q에 두 번째 원소와 첫 번째 요소의 차이를 저장합니다.
    Q = numbers[1] - numbers[0]
# 수열의 세 번째 원소를 두 번째 원소로 나눈 결과가
# 수열의 두 번째 원소를 첫 번째 원소로 나눈 결과와 같다면
elif numbers[2] / numbers[1] == numbers[1] / numbers[0]:
    # 등비수열이므로 difference_or_ratio 변수에 "ratio"를 저장해줍니다.
    difference_or_ratio = "ratio"
    # 공비 Q에 두 번째 원소와 첫 번째 요소의 비율을 정수형으로 변환하고 저장합니다.
    Q = int(numbers[1] / numbers[0])

# 등차수열이라면
if difference_or_ratio == "difference":
    # 입력한 맨 끝 원소에 공차 Q의 값을 더한 값을 출력합니다.
    print(numbers[-1] + Q)
# 등비수열이라면
else:
    # 입력한 맨 끝 원소에 공비 Q의 값을 곱한 값을 출력합니다.
    print(numbers[-1] * Q)