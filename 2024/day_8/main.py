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
    antena = []
    antena_verif = []
    antinodes = []
    sum = 0

    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            if (line[x] != '.'):
                antena.append([x, len(lines) - y - 1, line[x]])
    for v_antena in antena:
        for a_antena in antena:
            if (v_antena != a_antena and v_antena[2] == a_antena[2] and not [v_antena, a_antena] in antena_verif):
                distance_x = v_antena[0] - a_antena[0]
                distance_y = v_antena[1] - a_antena[1]
                if ((v_antena[0] + distance_x >= 0 and v_antena[0] + distance_x < len(lines[0])) and (v_antena[1] + distance_y >= 0 and v_antena[1] + distance_y < len(lines)) and not [v_antena[0] + distance_x, v_antena[1] + distance_y] in antinodes):
                    antinodes.append([v_antena[0] + distance_x, v_antena[1] + distance_y])
                    print("New 1:",v_antena,a_antena,antinodes[-1])
                if ((a_antena[0] - distance_x >= 0 and a_antena[0] - distance_x < len(lines[0])) and (a_antena[1] - distance_y >= 0 and v_antena[1] - distance_y < len(lines)) and not [a_antena[0] - distance_x, a_antena[1] - distance_y] in antinodes):
                    antinodes.append([a_antena[0] - distance_x, a_antena[1] - distance_y])
                    print("New 2:",v_antena,a_antena,antinodes[-1])
                antena_verif.append([v_antena, a_antena])
                antena_verif.append([a_antena, v_antena])
    for line in lines:
        print(line)
    print(antena)
    print(antinodes)
    print(len(antinodes))

def gold(lines):
    antena = []
    antena_type = []
    antena_verif = []
    antinodes = []
    sum = 0

    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            if (line[x] != '.'):
                antena.append([x, len(lines) - y - 1, line[x]])
                antena_type.append(line[x])
    for v_antena in antena:
        for a_antena in antena:
            if (v_antena != a_antena and v_antena[2] == a_antena[2] and not [v_antena, a_antena] in antena_verif):
                distance_x = v_antena[0] - a_antena[0]
                distance_y = v_antena[1] - a_antena[1]
                out = [False, False]
                i = 1
                while (not out[0] or not out[1] ):
                    if ((v_antena[0] + distance_x * i >= 0 and v_antena[0] + distance_x * i < len(lines[0])) and (v_antena[1] + distance_y * i >= 0 and v_antena[1] + distance_y * i < len(lines)) and not [v_antena[0] + distance_x * i, v_antena[1] + distance_y * i] in antinodes):
                        antinodes.append([v_antena[0] + distance_x * i, v_antena[1] + distance_y * i])
                        print("New 1:",v_antena,a_antena,antinodes[-1],i)
                    else:
                        out[0] = True
                    if ((a_antena[0] - distance_x * i >= 0 and a_antena[0] - distance_x * i < len(lines[0])) and (a_antena[1] - distance_y * i >= 0 and v_antena[1] - distance_y * i < len(lines)) and not [a_antena[0] - distance_x * i, a_antena[1] - distance_y * i] in antinodes):
                        antinodes.append([a_antena[0] - distance_x * i, a_antena[1] - distance_y * i])
                        print("New 2:",v_antena,a_antena,antinodes[-1],i)
                    else:
                        out[1] = True
                    i += 1
                antena_verif.append([v_antena, a_antena])
                antena_verif.append([a_antena, v_antena])
    for v_antena in antena:
        if (antena_type.count(v_antena[2]) > 1 and not [v_antena[0], v_antena[1]] in antinodes):
            antinodes.append([v_antena[0], v_antena[1]])
    for line in lines:
        print(line)
    print(antena)
    print(antinodes)
    print(antena_type)
    print(len(antinodes))

gold(lines)
