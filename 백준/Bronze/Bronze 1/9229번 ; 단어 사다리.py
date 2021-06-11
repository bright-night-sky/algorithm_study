# https://www.acmicpc.net/problem/9229

from sys import stdin

while True:
    prev_word = stdin.readline().rstrip()
    prev_word_len = len(prev_word)
    can_ladder = 'Correct'

    if prev_word == '#':
        break

    while True:
        next_word = stdin.readline().rstrip()
        next_word_len = len(next_word)
        diff_cnt = 0

        if next_word == '#':
            break

        if prev_word_len != next_word_len:
            can_ladder = 'Incorrect'
            break

        for char_idx in range(next_word_len):
            if prev_word[char_idx] != next_word[char_idx]:
                diff_cnt += 1

        if diff_cnt != 1:
            can_ladder = 'Incorrect'
            break

    print(can_ladder)