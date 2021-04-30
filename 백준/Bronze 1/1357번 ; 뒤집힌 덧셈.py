# https://www.acmicpc.net/problem/1357

# 문제의 Rev(X) 함수를 구현합니다.
# 매개변수로 숫자로 이루어진 문자열 X를 하나 받습니다.
def Rev(X):
    # 문자열 X를 뒤집고 정수형으로 만들어줍니다.
    X = int(X[::-1])

    # 뒤집어진 정수형 X를 반환합니다.
    return X

# 첫째 줄에 X, Y를 입력합니다.
# X, Y는 1,000보다 작거나 같은 자연수입니다.
X, Y = input().split(' ')

# Rev(Rev(X) + Rev(Y))를 계산합니다.
# Rev(X) + Rev(Y)는 정수형인데, Rev 함수는 문자열 형태의 인수를 받으므로
# str(Rev(X) + Rev(Y))로 문자열 형태로 변환해서 넣어줍니다.
result = Rev(str(Rev(X) + Rev(Y)))

# 계산 결과를 출력합니다.
print(result)