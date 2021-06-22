# https://www.acmicpc.net/problem/2309

from sys import stdin


dwarfs = [None] * 9

for idx in range(9):
    dwarf_tall = int(stdin.readline())
    dwarfs[idx] = dwarf_tall

dwarfs.sort()
nine_talls_sum = sum(dwarfs)

for i in range(7):
    for j in range(i + 1, 8):
        for k in range(j + 1, 9):
            seven_talls_sum = nine_talls_sum - (dwarfs[i] + dwarfs[j] + dwarfs[k])

            if seven_talls_sum == 100:
                dwarfs.remove(dwarfs[i])
                dwarfs.remove(dwarfs[j])
                dwarfs.remove(dwarfs[k])


for tall in dwarfs:
    print(tall)