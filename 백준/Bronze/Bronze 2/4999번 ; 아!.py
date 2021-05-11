# https://www.acmicpc.net/problem/4999

# 첫째 줄에 재환이가 가장 길게 낼 수 있는 "aaah"를 입력합니다.
jaehwan_aaah = input()

# 둘째 줄에 의사가 듣기를 원하는 "aah"를 입력합니다.
doctor_aah = input()

# 재환이가 가장 길게 낼 수 있는 "aaah"의 길이를 저장하는 변수를 선언합니다.
jaehwan_aaah_length = len(jaehwan_aaah)
# 의사가 가장 길게 낼 수 있는 "aah"의 길이를 저장하는 변수를 선언합니다.
doctor_aah_length = len(doctor_aah)

# 재환이가 가장 길게 낼 수 있는 "aaah"의 길이가
# 의사가 가장 길게 낼 수 있는 "aah"의 길이보다 길거나 같다면
if jaehwan_aaah_length >= doctor_aah_length:
    # go를 출력합니다.
    print("go")
# 재환이가 가장 길게 낼 수 있는 "aaah"의 길이가
# 의사가 가장 길게 낼 수 있는 "aah"의 길이보다 작다면
else:
    # no를 출력합니다.
    print("no")