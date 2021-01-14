# https://www.acmicpc.net/problem/10707

# 첫 번째 줄에는 X사의 1리터당 요금 A 입력
A = int(input())
# 두 번째 줄에는 Y사의 기본요금 B 입력
B = int(input())
# 세 번째 줄에는 Y사의 요금이 기본요금이 되는 사용량의 상한 C 입력
C = int(input())
# 네 번째 줄에는 Y사의 1리터 당 추가요금 D 입력
D = int(input())
# 다섯 번째 줄에는 JOI군의 집에서 사용하는 한 달간 수도의 양 P 입력
P = int(input())
# 1 <= A, B, C, D, P <= 10,000

# JOI 군이 X사를 이용하는 경우 수도요금 계산
X_charge = A * P
# JOI 군이 Y사를 이용하는 경우 수도요금 계산
Y_charge = B
if P > C:
    Y_charge += (P - C) * D

# X사와 Y사를 이용했을 때 더 적게 내는 수도요금을 출력
print(min(X_charge, Y_charge))