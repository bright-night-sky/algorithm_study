# https://www.acmicpc.net/problem/8949

# 두 정수 A, B를 공백을 두고 입력합니다.
# A, B는 1과 1,000,000 사이의 정수입니다.
A, B = input().split(' ')

# 입력한 A를 거꾸로 배치한 뒤 각 자리 숫자들을 정수형으로 만들고 리스트 변수에 넣어줍니다.
A = list(map(int, A[::-1]))
# 입력한 B를 거꾸로 배치한 뒤 각 자리 숫자들을 정수형으로 만들고 리스트 변수에 넣어줍니다.
B = list(map(int, B[::-1]))

# A의 길이를 저장하는 변수를 선언합니다.
A_length = len(A)
# B의 길이를 저장하는 변수를 선언합니다.
B_length = len(B)

# A의 길이와 B의 길이 중 더 작은 값을 저장하는 변수를 선언합니다.
min_length = min(A_length, B_length)

# 각 자리 숫자의 합을 저장할 리스트 변수를 선언합니다.
plus_results = []

# A의 길이와 B의 길이 중 더 짧은 길이만큼 반복합니다.
for index in range(min_length):
    # A와 B의 같은 자리 숫자를 더한 변수를 선언합니다.
    AB_plus = A[index] + B[index]
    # 그 더한 값을 plus_results에 넣어줍니다.
    plus_results.append(AB_plus)

# A의 길이가 B의 길이보다 길다면
if A_length > B_length:
    # plus_results에 A의 남은 자리 숫자들을 추가해줍니다.
    plus_results.extend(A[min_length:])
# A의 길이가 B의 길이보다 작다면
elif A_length < B_length:
    # plus_results에 B의 남은 자리 숫자들을 추가해줍니다.
    plus_results.extend(B[min_length:])

# 더한 결과들을 다시 뒤집어 줍니다.
plus_results = plus_results[::-1]

# 더한 결과들을 하나씩 출력해줍니다.
for number in plus_results:
    print(number, end='')