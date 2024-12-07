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

def silver(lines):
    sum = 0
    out = False

    while (True):
        for y in range(len(lines)):
            line = lines[y]
    
            for x in range(len(line)):
                if (line[x] == '^'):
                    if (y == 0):
                        out = True
                        break
                    if (lines[y - 1][x] == '.' or lines[y - 1][x] == 'x'):
                        lines[y][x] = 'x'
                        lines[y - 1][x] = '^'
                    else:
                        lines[y][x] = '>'
                elif (line[x] == '>'):
                    if (x == len(line) - 1):
                        out = True
                        break
                    if (lines[y][x + 1] == '.' or lines[y][x + 1] == 'x'):
                        lines[y][x] = 'x'
                        lines[y][x + 1] = '>'
                    else:
                        lines[y][x] = 'v'
                elif (line[x] == 'v'):
                    if (y == len(lines) - 1):
                        out = True
                        break
                    if (lines[y + 1][x] == '.' or lines[y + 1][x] == 'x'):
                        lines[y][x] = 'x'
                        lines[y + 1][x] = 'v'
                    else:
                        lines[y][x] = '<'
                elif (line[x] == '<'):
                    if (x == 0):
                        out = True
                        break
                    if (lines[y][x - 1] == '.' or lines[y][x - 1] == 'x'):
                        lines[y][x] = 'x'
                        lines[y][x - 1] = '<'
                    else:
                        lines[y][x] = '^'
            if (out):
                break
        if (out):
            break
    for line in lines:
        for c in line:
            if (c == 'x'):
                sum += 1
    for line in lines:
        print(line)
    print(sum + 1)

def gold(lines):
    sum = 0
    cos = []
    co_true = []

    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            if (lines[y][x] == '#'):
                cos.append([x,y])
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            start_co = [x, y]
            tp_r_co = []
            bot_l_co = []
            tp_r = False
            tp_l = False
            bot_r = False
            bot_l = False
            if (start_co in cos):
                tp_l = True
            for co in cos:
                if (start_co[1] + 1 == co[1] and start_co[0] < co[0]):
                    tp_r = True
                    tp_r_co = co
            for co in cos:
                if (start_co[0] - 1 == co[0] and start_co[1] < co[1]):
                    bot_l = True
                    bot_l_co = co
            if ((not tp_l and not tp_r) or (not tp_l and not bot_l) or (not tp_r and not bot_l)):
                print("Out:",start_co,tp_l,tp_r,bot_l)
                continue
            print("Continue:",start_co,tp_l,tp_r,bot_l)
            if (not tp_l):
                for co in cos:
                    if (tp_r_co[0] - 1 == co[0] and tp_r_co[1] < co[1] and bot_l_co[1] + 1 == co[1] and bot_l_co[0] < co[0]):
                        bot_r = True
            elif (not tp_r):
                for co in cos:
                    if (bot_l_co[1] + 1 == co[1] and bot_l_co[0] < co[0]):
                        bot_r = True
            elif (not bot_l):
                for co in cos:
                    if (tp_r_co[0] - 1 == co[0] and tp_r_co[1] < co[1]):
                        bot_r = True
            if (bot_r or (tp_r and tp_l and bot_l)):
                print("TRUE:",start_co,tp_l,tp_r,bot_l,bot_r)
                co_true.append(start_co)
                sum += 1
    for line in lines:
        print(line)
    print(cos)
    print(co_true)
    print(sum)

def gold_v2(lines):
    sum = 0
    out = False

    while (True):
        for y in range(len(lines)):
            line = lines[y]
    
            for x in range(len(line)):
                if (line[x] == '^'):
                    if (y == 0):
                        out = True
                        break
                    if (lines[y - 1][x] == '.' or lines[y - 1][x] == 'x'):
                        lines[y][x] = 'x'
                        lines[y - 1][x] = '^'
                    else:
                        lines[y][x] = '>'
                elif (line[x] == '>'):
                    if (x == len(line) - 1):
                        out = True
                        break
                    if (lines[y][x + 1] == '.' or lines[y][x + 1] == 'x'):
                        lines[y][x] = 'x'
                        lines[y][x + 1] = '>'
                    else:
                        lines[y][x] = 'v'
                elif (line[x] == 'v'):
                    if (y == len(lines) - 1):
                        out = True
                        break
                    if (lines[y + 1][x] == '.' or lines[y + 1][x] == 'x'):
                        lines[y][x] = 'x'
                        lines[y + 1][x] = 'v'
                    else:
                        lines[y][x] = '<'
                elif (line[x] == '<'):
                    if (x == 0):
                        out = True
                        break
                    if (lines[y][x - 1] == '.' or lines[y][x - 1] == 'x'):
                        lines[y][x] = 'x'
                        lines[y][x - 1] = '<'
                    else:
                        lines[y][x] = '^'
            if (out):
                break
        if (out):
            break
    for line in lines:
        for c in line:
            if (c == 'x'):
                sum += 1
    for line in lines:
        print(line)
    print(sum + 1)

gold_v2(lines)
