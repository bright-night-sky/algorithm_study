# https://www.acmicpc.net/problem/11816

# 첫째 줄에 X를 입력합니다.
# X는 10진수로 바꿨을 때, 1,000,000보다 작거나 같은 자연수입니다.
# 16진수인 경우 알파벳은 소문자로만 이루어져 있습니다.
X = input()

# 입력한 X의 값에서 앞의 두 자리가 0x라면
if X[0:2] == "0x":
    # 입력한 X를 16진수로 간주하고 10진수로 바꿔 출력합니다.
    print(int(X, 16))
# 입력한 X의 값에서 앞의 한 자리가 0라면
elif X[0] == "0":
    # 입력한 X를 8진수로 간주하고 10진수로 바꿔 출력합니다.
    print(int(X, 8))
# 그 외의 경우에는
else:
    # 입력한 X를 10진수로 간주하고 10진수 그대로 출력합니다.
    print(X)