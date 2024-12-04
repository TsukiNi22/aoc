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
    lines.append(line.split())
    for i in range(len(lines[-1])):
        lines[-1][i] = int(lines[-1][i])
    lines[-1] = list(map(lambda nbr: int(nbr), lines[-1]))

def silver(lines):
    print(lines)

def gold(lines):
    print(lines)

silver(lines)
