# https://www.acmicpc.net/problem/21312

from sys import stdin


drinks = list(map(int, stdin.readline().split(' ')))
odd_cocktails = []
even_cocktails = []

for i in range(0, 2):
    for j in range(i + 1, 3):
        cocktail = drinks[i] * drinks[j]

        if cocktail % 2 == 0:
            even_cocktails.append(cocktail)
        else:
            odd_cocktails.append(cocktail)

if odd_cocktails != []:
    print(max(odd_cocktails))
else:
    print(max(even_cocktails))