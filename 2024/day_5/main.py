##
## PHYTON PROJECT, 2024
## main.py
## File description:
## You know, I don t think there are good or bad descriptions,
## for me, life is above all about functions...
##

rules = []
lines = []
rule = True
while True:
    line = input()
    if line.lower() == 's':
         break
    if (line == ""):
        rule = False
        continue
    if (rule):
        rules.append(line.split('|'))
        rules[-1] = list(map(lambda nbr: int(nbr), rules[-1]))
    else:
        lines.append(line.split(','))
        lines[-1] = list(map(lambda nbr: int(nbr), lines[-1]))

def silver(rules, lines):
    sum = 0

    for i in range(len(lines)):
        line = lines[i]
        line_verif = True

        for j in range(len(line)):
            actual_rules = []
            
            for rule in rules:
                if (rule[0] == line[j]):
                    actual_rules.append(rule[1])
            for k in range(j):
                if (line[k] in actual_rules):
                    line_verif = False
                    break
            if (not line_verif):
                break
        if (line_verif):
            print(line)
            sum += line[int(len(line) / 2)]
    print(sum)

def gold(rules, lines):
    sum = 0

    for i in range(len(lines)):
        line = lines[i]
        line_sort = lines[i]
        line_verif = True
        j = 0

        while (j < len(line)):
            actual_rules = []
            reset = False
            
            for rule in rules:
                if (rule[0] == line[j]):
                    actual_rules.append(rule[1])
            for k in range(j):
                if (line[k] in actual_rules):
                    line_verif = False
                    reset = True
                    print(line, j, k, line_sort)
                    line_sort.insert(k, line_sort.pop(j))
                    j = 0
                    break
            if (not reset):
                j += 1
        if (not line_verif):
            print(line)
            print(line_sort)
            sum += line_sort[int(len(line_sort) / 2)]
    print(sum)

gold(rules, lines)
