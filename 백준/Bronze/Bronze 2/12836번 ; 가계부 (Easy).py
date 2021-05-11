# https://www.acmicpc.net/problem/12836

# 첫째 줄에 월곡이가 살아온 날 N, 쿼리의 개수 Q를 입력합니다.
# N <= 10^4
# Q <= 10^3
N, Q = map(int, input().split(' '))

# 생후 p일에서 p-1을 각 index로 생각하고
# 그 index에서의 값을 해당 p일의 수입/지출 x로 설정할
# 가계부 리스트 변수를 만들어줍니다.
# 살아온 날 N개만큼 None을 넣어줍니다.
household_account = [None for x in range(N)]

# 쿼리의 개수 Q만큼 반복합니다.
for i in range(Q):
    # 1 p x 혹은 2 p q 형태의 쿼리를 입력합니다.
    query_type, p, x_or_q = map(int, input().split(' '))

    # 입력한 쿼리가 1 p x 형태인데
    if query_type == 1:
        # 아직 가계부에 해당 날짜에 대한 수입/지출을 입력한 적이 없다면
        # 즉 None이라면
        if household_account[p-1] is None:
            # 수입/지출 값을 넣어줍니다.
            household_account[p-1] = x_or_q
        # 앞선 쿼리에서 해당 날짜에 대한 수입/지출을 입력한 적이 있다면
        else:
            # 수입/지출 값을 더해줍니다.
            household_account[p-1] += x_or_q
    # 입력한 쿼리가 2 p q 형태라면
    else:
        # 총 변화한 양을 저장할 변수 variance를 만들어줍니다.
        variance = 0

        # 생후 p일부터 q일까지 반복합니다.
        for j in range(p, x_or_q+1):
            # p일부터 q일까지 반복하면서
            # None값이 아닌 값이 있다면 즉, 수입/지출 값이 있다면
            if household_account[j-1] is not None:
                # variance에 수입/지출 값을 더해줍니다.
                variance += household_account[j-1]

        # 총 변화한 양을 저장한 변수 variance의 값을 출력합니다.
        print(variance)