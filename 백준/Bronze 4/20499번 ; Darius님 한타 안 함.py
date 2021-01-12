# https://www.acmicpc.net/problem/20499

# K/D/A 형식으로 입력
# 0 <= K, D, A <= 20
# 입력할 때 중간에 /가 있으므로 문자열을 정리해서 각 변수에 저장
K, D, A = map(int, input().split('/'))

# K + A < D이거나, D = 0이면
if (K + A) < D or D == 0:
    # 가짜이므로 hasu 출력
    print("hasu")
# 그렇지 않으면,
else:
    # 진짜이므로 gosu 출력
    print("gosu")