# https://www.acmicpc.net/problem/4732

from sys import stdin

scale = ('A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#')

while True:
    note_order = stdin.readline().rstrip()

    if note_order == '***':
        break

    note_order = note_order.split(' ')

    transpose = int(stdin.readline())

    for note in note_order:
        note_idx_in_scale = None

        if note[-1] == 'b':
            note = note[:-1]
            print(note)
            note_idx_in_scale = scale.index(note) - 1
        else:
            note_idx_in_scale = scale.index(note)

        transpose_result = note_idx_in_scale + transpose

        if transpose_result > len(scale):
            transpose_result -= len(scale)

        print(scale[transpose_result], end=' ')