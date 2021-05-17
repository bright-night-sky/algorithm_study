# https://www.acmicpc.net/problem/1755

from sys import stdin

M, N = map(int, stdin.readline().split(' '))

number_to_english = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

number_and_english = []

for number in range(M, N + 1):
    number = str(number)