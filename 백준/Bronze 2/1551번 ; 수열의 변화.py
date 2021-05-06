# https://www.acmicpc.net/problem/1551

# 첫째 줄에 수열의 크기 N, 방법 K번을 입력합니다.
# N은 20보다 작거나 같은 자연수이고,
# K는 0보다 크거나 같고, N-1보다 작거나 같은 자연수입니다.
N, K = map(int, input().split(' '))

# 수열을 ,로 구분해서 입력합니다.
sequence = list(map(int, input().split(',')))

# 다음 수열을 임시로 저장하는 리스트 변수를 선언합니다.
temp = []

# 새로운 수열을 만드는 방법을 K번 반복합니다.
for method_index in range(K):
    # 수열의 마지막에서 두 번째 원소까지 반복합니다.
    for sequence_index in range(len(sequence) - 1):
        # A[i+1] - A[i]를 temp에 넣어줍니다.
        temp.append(sequence[sequence_index + 1] - sequence[sequence_index])

    # sequence의 값을 temp 리스트로 바꿔줍니다.
    sequence = temp
    # temp의 값을 빈 리스트로 만들어줍니다.
    temp = []

# 최종적으로 나온 수열의 각 원소들을 문자열 형태로 변환해줍니다.
sequence = list(map(str, sequence))

# 출력 형식에 맞게 출력해줍니다.
print(','.join(sequence))