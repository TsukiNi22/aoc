##
## PHYTON PROJECT, 2024
## main.py
## File description:
## You know, I don t think there are good or bad descriptions,
## for me, life is above all about functions...
##

from re import *

lines = []
while True:
    line = input()
    if line.lower() == 's':
        break
    lines.append(list(line))

def droite(lines, x ,y):
    if (x > len(lines[y]) - 4):
        return 0
    if (lines[y][x] == 'X' and lines[y][x + 1] == 'M' and lines[y][x + 2] == 'A' and lines[y][x + 3] == 'S'):
        return 1
    return 0

def gauche(lines, x ,y):
    if (x < 3):
        return 0
    if (lines[y][x] == 'X' and lines[y][x - 1] == 'M' and lines[y][x - 2] == 'A' and lines[y][x - 3] == 'S'):
        return 1
    return 0

def haut(lines, x ,y):
    if (y < 3):
        return 0
    if (lines[y][x] == 'X' and lines[y - 1][x] == 'M' and lines[y - 2][x] == 'A' and lines[y - 3][x] == 'S'):
        return 1
    return 0

def bas(lines, x ,y):
    if (y > len(lines) - 4):
        return 0
    if (lines[y][x] == 'X' and lines[y + 1][x] == 'M' and lines[y + 2][x] == 'A' and lines[y + 3][x] == 'S'):
        return 1
    return 0

def droite_haut(lines, x ,y):
    if (y < 3 or x > len(lines[y]) - 4):
        return 0
    if (lines[y][x] == 'X' and lines[y - 1][x + 1] == 'M' and lines[y - 2][x + 2] == 'A' and lines[y - 3][x + 3] == 'S'):
        return 1
    return 0

def droite_bas(lines, x ,y):
    if (y > len(lines) - 4 or x < 3):
        return 0
    if (lines[y][x] == 'X' and lines[y + 1][x - 1] == 'M' and lines[y + 2][x - 2] == 'A' and lines[y + 3][x - 3] == 'S'):
        return 1
    return 0

def gauche_haut(lines, x ,y):
    if (y < 3 or x < 3):
        return 0
    if (lines[y][x] == 'X' and lines[y - 1][x - 1] == 'M' and lines[y - 2][x - 2] == 'A' and lines[y - 3][x - 3] == 'S'):
        return 1
    return 0

def gauche_bas(lines, x ,y):
    if (y > len(lines) - 4 or x > len(lines[y]) - 4):
        return 0
    if (lines[y][x] == 'X' and lines[y + 1][x + 1] == 'M' and lines[y + 2][x + 2] == 'A' and lines[y + 3][x + 3] == 'S'):
        return 1
    return 0

def silver(lines):
    total = 0

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            total += droite(lines, x, y)
            total += gauche(lines, x, y)
            total += haut(lines, x ,y)
            total += bas(lines, x ,y)
            total += droite_haut(lines, x ,y)
            total += droite_bas(lines, x ,y)
            total += gauche_haut(lines, x ,y)
            total += gauche_bas(lines, x ,y)
    print(lines)
    print(total)

def gold(lines):
    x_max = len(lines[-1])
    y_max = len(lines)
    total = 0

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if (x < 1 or y < 1 or x > x_max - 2 or y > y_max - 2):
                continue
            if (lines[y][x] != 'A'):
                continue
            if (not ((lines[y + 1][x - 1] == 'M' and lines[y - 1][x + 1] == 'S') or (lines[y + 1][x - 1] == 'S' and lines[y - 1][x + 1] == 'M'))):
                continue
            if (not ((lines[y - 1][x - 1] == 'M' and lines[y + 1][x + 1] == 'S') or (lines[y - 1][x - 1] == 'S' and lines[y + 1][x + 1] == 'M'))):
                continue
            total += 1
    print(lines)
    print(total)

gold(lines)
