# https://www.acmicpc.net/problem/2752

# 숫자 세 개 입력받고 리스트에 저장
# 1 <= 숫자 세 개 <= 1,000,000
num = list(map(int, input().split(' ')))

# num 리스트 안에 있는 숫자를 오름차순으로 정렬
num = sorted(num)

# 오름차순 정렬이 된 num의 숫자 세 개를 차례로 출력
for i in num:
    print(i, end=' ')