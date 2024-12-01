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
    lines.append(line)

def main_silver(lines):
    lines_split = [line.split() for line in lines]
    first_col = []
    second_col = []
    sum = 0

    for i in range(len(lines_split)):
        first_col.append(int(lines_split[i][0]))
        second_col.append(int(lines_split[i][1]))
    first_col = sorted(first_col)
    second_col = sorted(second_col)
    for i in range(len(first_col)):
        sum += abs(first_col[i] - second_col[i])
    print(sum)

def main_gold(lines):
    lines_split = [line.split() for line in lines]
    first_col = []
    second_col = []
    sum = 0

    for i in range(len(lines_split)):
        first_col.append(int(lines_split[i][0]))
        second_col.append(int(lines_split[i][1]))
    second_col = sorted(second_col)
    for i in range(len(first_col)):
        mult = 0
        for j in range(len(second_col)):
            if first_col[i] == second_col[j]:
                mult += 1
        sum += first_col[i] * mult
    print(sum)

main_gold(lines)
