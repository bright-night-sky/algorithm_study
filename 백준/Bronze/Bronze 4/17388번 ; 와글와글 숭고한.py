# https://www.acmicpc.net/problem/17388

# 숭실대학교의 참여도, 고려대학교의 참여도, 한양대학교의 참여도인 S, K, H 입력
# 0 <= S, K, H <= 100
univ = list(map(int, input().split(' ')))

# 세 대학교의 참여도를 합친 결과를 저장하는 변수
participation = sum(univ)

# 참여도가 100 미만인 경우 가장 낮은 참여도를 가진 대학교를 저장할 변수
min_univ = ''

# 세 대학교의 참여도의 합이 100 이상이면
if participation >= 100:
    # OK 출력
    print("OK")
# 세 대학교의 참여도의 합이 100 미만이면
else:
    # 가장 낮은 참여도를 가진 대학교를 출력
    # 대학교들의 참여도를 가장 낮은 참여도와 비교
    for idx in range(0, len(univ)):
        if min(univ) == univ[idx]:
            # 인덱스 0이 가장 낮은 값이면 숭실대학교의 참여도가 제일 낮은 것이다.
            if idx == 0:
                print("Soongsil")
            # 인덱스 1이 가장 낮은 값이면 고려대학교의 참여도가 제일 낮은 것이다.
            elif idx == 1:
                print("Korea")
            # 인덱스 2가 가장 낮은 값이면 한양대학교의 참여도가 제일 낮은 것이다.
            else:
                print("Hanyang")