# https://www.acmicpc.net/problem/5596

# 1번째 줄에 민국이의 정보, 수학, 과학 영어 점수(정수형) 입력 : 공백으로 구분
minguk = list(map(int, input().split(" ")))
# 2번째 줄에 만세의 정보, 수학, 과학, 영어 점수(정수형) 입력 : 공백으로 구분
manse = list(map(int, input().split(" ")))

# 민국이의 총점을 저장하는 변수
minguk_total = sum(minguk)
# 만세의 총점을 저장하는 변수
manse_total = sum(manse)

# 민국이의 총점이 만세의 총점보다 큰 경우
if minguk_total > manse_total:
    # 민국이의 총점을 출력
    print(minguk_total)
# 만세의 총점이 민국이의 총점보다 큰 경우
elif minguk_total < manse_total:
    # 만세의 총점을 출력
    print(manse_total)
# 둘의 총점이 같은 경우
else:
    # 민국이의 총점을 출력
    print(minguk_total)