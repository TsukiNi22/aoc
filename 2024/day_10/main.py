##
## PHYTON PROJECT, 2024
## main.py
## File description:
## You know, I don t think there are good or bad descriptions,
## for me, life is above all about functions...
##

lines = []
while True:
    line = input()
    if line.lower() == 's':
        break
    lines.append(list(line))
    lines[-1] = list(map(lambda nbr: int(nbr), lines[-1]))

def silver(lines):
    total = 0

    def rec(x, y, val):
        sum = 0

        if (x >= len(lines[-1]) or x < 0 or y >= len(lines) or y < 0 or lines[y][x] != val):
            return 0
        if (val == 9):
            return 1
        sum += rec(x + 1, y, val + 1)
        sum += rec(x - 1, y, val + 1)
        sum += rec(x, y + 1, val + 1)
        sum += rec(x, y - 1, val + 1)
        return sum

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if (lines[y][x] == 0):
                total += rec(x, y, 0)
    print(lines)
    print(total)

def gold(lines):
    total = 0
    point = []

    def rec(x, y, val):
        sum = 0

        if (x >= len(lines[-1]) or x < 0 or y >= len(lines) or y < 0 or lines[y][x] != val):
            return 0
        if (val == 9):
            if ([x, y] in point):
                return 0
            point.append([x, y])
            return 1
        sum += rec(x + 1, y, val + 1)
        sum += rec(x - 1, y, val + 1)
        sum += rec(x, y + 1, val + 1)
        sum += rec(x, y - 1, val + 1)
        return sum

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if (lines[y][x] == 0):
                point = []
                total += rec(x, y, 0)
    print(lines)
    print(total)


silver(lines)
