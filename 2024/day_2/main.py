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

def silver(lines):
    lines_split = [line.split() for line in lines]
    report_true = 0

    for line in lines_split:
        signe = -1

        for i in range(len(line) - 1):
            dif = int(line[i]) - int(line[i + 1])
            if (signe == -1 and dif < 0):
                signe = 1
            elif (signe == -1):
                signe = 0
            if (signe == 1 and not (dif <= -1 and dif >= -3)):
                break
            if (signe == 0 and not (dif >= 1 and dif <= 3)):
                break
            if (i == len(line) - 2):
                report_true += 1
    print(report_true)

def gold(lines):
    lines_split = [line.split() for line in lines]
    report_true = 0

    for line in lines_split:
        signe = -1
        joker = 0
        i = 0

        if (len(line) == 1 or len(line) == 2):
            report_true += 1
            print(line)
            continue
        while (i < len(line) - 1):
            dif = int(line[i]) - int(line[i + 1])
            print(line[i], line[i + 1], i, dif, joker, signe, line)
            if (i + 1 == len(line) and joker == 0):
                report_true += 1
                print(line)
                break
            if (signe == -1 and dif < 0):
                if (not (dif <= -1 and dif >= -3)):
                    joker += 1
                    if (joker > 1):
                        break
                    if (i - 1 < 0):
                        dif = int(line[i]) - int(line[i + 2])
                        i += 1
                    else:
                        dif = int(line[i - 1]) - int(line[i + 1])
                    if (i + 2 == len(line) - 1):
                        report_true += 1
                        print(line)
                    break
                    if (not (dif <= -1 and dif >= -3) and not (dif >= 1 and dif <= 3)):
                        break
                if (dif < 0):
                    signe = 1
                else:
                    signe = 0
                i += 1
                continue
            elif (signe == -1):
                if (not (dif >= 1 and dif <= 3)):
                    joker += 1
                    dif = int(line[i - 1]) - int(line[i + 1])
                    i += 1
                    if (joker > 1):
                        break
                    if (i - 1 < 0):
                        dif = int(line[i]) - int(line[i + 2])
                        i += 1
                    else:
                        dif = int(line[i - 1]) - int(line[i + 1])
                    if (i + 2 == len(line) - 1):
                        report_true += 1
                        print(line)
                    break
                    if (not (dif <= -1 and dif >= -3) and not (dif >= 1 and dif <= 3)):
                        break
                if (dif < 0):
                    signe = 1
                else:
                    signe = 0
                i += 1
                continue
            if (signe == 1 and not (dif <= -1 and dif >= -3)):
                joker += 1
                if (joker > 1):
                    break
                if (i + 1 == len(line) - 1):
                    report_true += 1
                    print(line)
                    break
                dif = int(line[i - 1]) - int(line[i + 1])
                if (not (dif <= -1 and dif >= -3)):
                    break
            if (signe == 0 and not (dif >= 1 and dif <= 3)):
                joker += 1
                dif = int(line[i - 1]) - int(line[i + 1])
                if (joker > 1):
                    break
                if (i + 1 == len(line) - 1):
                    report_true += 1
                    print(line)
                    break
                if (not (dif >= 1 and dif <= 3)):
                    break
            if (i == len(line) - 2):
                report_true += 1
                print(line)
            i += 1
    print(report_true)

def gold_v2(lines):
    lines_split = [line.split() for line in lines]
    report_true = 0

    for line in lines_split:
        signe = -1
        joker = 0
        i = 0

        if (len(line) == 1 or len(line) == 2):
            report_true += 1
            print(line)
            continue
        while (i < len(line) - 1):
            dif = int(line[i]) - int(line[i + 1])
            print(line[i], line[i + 1], i, dif, line)
            if (signe == -1 and dif < 0):
                signe = 1
            elif (signe == -1):
                signe = 0
            if (signe == 1 and not (dif <= -1 and dif >= -3)):
                joker += 1
                if (joker > 1):
                    break
                if (i == 0):
                    signe = -1
                    i += 1
                    continue
                elif (i == len(line) - 2):
                    report_true += 1
                    print(line)
                    break
                dif_tmp = int(line[i]) - int(line[i + 2])
                signe_tmp = 0
                if (dif_tmp < 0):
                    signe_tmp = 1
                if (signe_tmp == 1 and not (dif_tmp <= -1 and dif_tmp >= -3)):
                    break
                elif (signe_tmp == 0  and not (dif_tmp >= 1 and dif_tmp <= 3)):
                    break
                i += 1
            elif (signe == 0 and not (dif >= 1 and dif <= 3)):
                joker += 1
                if (joker > 1):
                    break
                if (i == 0):
                    signe = -1
                    i += 1
                    continue
                elif (i == len(line) - 2):
                    report_true += 1
                    print(line)
                    break
                dif_tmp = int(line[i]) - int(line[i + 2]) 
                signe_tmp = 0
                if (dif_tmp < 0):
                    signe_tmp = 1
                if (signe_tmp == 1 and not (dif_tmp <= -1 and dif_tmp >= -3)):
                    break
                elif (signe_tmp == 0 and not (dif_tmp >= 1 and dif_tmp <= 3)):
                    break
                i += 1
            if (i == len(line) - 2):
                report_true += 1
                print(line)
            i += 1
    print(report_true)

def silver_v2(lines):
    lines_split = [line.split() for line in lines]
    report_true = 0

    for line in lines_split:
        pos = all(int(line[i]) < int(line[i + 1]) for i in range(len(line) - 1))
        neg = all(int(line[i]) > int(line[i + 1]) for i in range(len(line) - 1))

        if not (pos or neg):
            continue
        report = True
        for i in range(len(line) - 1):
            if not (1 <= abs(int(line[i]) - int(line[i + 1])) <= 3):
                report = False
                break
        if (report):
            report_true += 1
    print(report_true)
    return report_true

def safe(line):
    pos = all(int(line[i]) < int(line[i + 1]) for i in range(len(line) - 1))
    neg = all(int(line[i]) > int(line[i + 1]) for i in range(len(line) - 1))
    
    if not (pos or neg):
        return False
    for i in range(len(line) - 1):
        if not (1 <= abs(int(line[i]) - int(line[i + 1])) <= 3):
            return False
    return True

def gold_v3(lines):
    lines_split = [line.split() for line in lines]
    report_true = 0

    for line in lines_split:
        if safe(line):
            report_true += 1
            continue
        report = False
        for i in range(len(line)):
            line_tmp = line[:i] + line[i + 1:]
            if safe(line_tmp):
                report = True
                report_true += 1
                break
    print(report_true)

gold_v3(lines)
