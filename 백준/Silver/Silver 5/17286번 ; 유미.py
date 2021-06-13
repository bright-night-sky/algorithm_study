# https://www.acmicpc.net/problem/17286

from sys import stdin


yumi_position = list(map(int, stdin.readline().split(' ')))
people_positions = [None] * 3
shortest_distance = 0

for person_idx in range(3):
    person_position = list(map(int, stdin.readline().split(' ')))

    people_positions[person_idx] = person_position

for _ in range(3):
    shortest = 0
    shortest_person = None

    for person_position in people_positions:
        distance = ((yumi_position[0] - person_position[0]) ** 2 + (yumi_position[1] - person_position[1]) ** 2) ** 0.5

        if distance < shortest:
            shortest = distance
            shortest_person = person_position

    shortest_distance += shortest
    people_positions.remove(person_position)

print(int(shortest_distance))
