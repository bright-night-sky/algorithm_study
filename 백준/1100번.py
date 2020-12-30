# https://www.acmicpc.net/problem/1100

white_room_object = 0

for i in range(0, 8):
    line = input()

    if i % 2 == 0:
        for j in range(0, 8, 2):
            if line[j] == 'F':
                white_room_object += 1
    else:
        for j in range(1, 8, 2):
            if line[j] == 'F':
                white_room_object += 1

print(white_room_object)
