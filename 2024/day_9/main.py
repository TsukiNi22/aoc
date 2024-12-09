##
## PHYTON PROJECT, 2024
## main.py
## File description:
## You know, I don t think there are good or bad descriptions,
## for me, life is above all about functions...
##

line = list(open("input", "r").readline().strip())

def silver(line):
    new_line = []
    state = True
    id = 0

    for letter in line:
        for i in range(int(letter)):
            if (state):
                new_line.append(id)
            else:
                new_line.append('.')
        state = not state
        if (state):
            id += 1
    
    id = 0
    i = 0
    compact_line = new_line[:]
    for letter in reversed(new_line):
        if (letter == '.'):
            i += 1
            continue
        while (compact_line[id] != '.'):
            id += 1
        if (id >= len(compact_line) - i - 1):
            break
        compact_line[id] = letter
        compact_line[i * -1 - 1] = '.'
        i += 1
    
    sum = 0
    mult = 0
    for letter in compact_line:
        if (letter == '.'):
            mult += 1
            continue
        sum += mult * int(letter)
        mult += 1
    print(line)
    print(new_line)
    print(compact_line)
    print(sum)

def gold(line):
    new_line = []
    file_size = []
    place_loc = []
    state = True
    place_id = 0
    id = 0

    for letter in line:
        if (state):
            file_size.append([id, int(letter), place_id])
        for i in range(int(letter)):
            if (state):
                new_line.append(id)
            else:
                new_line.append('.')
        state = not state
        if (state):
            id += 1
        place_id += int(letter)
    
    def get_loc():
        loc = 0
        place_loc = []
        while(loc < len(new_line)):
            size = 0
            place = False
            for letter in compact_line[loc:]:
                if (place and letter != '.'):
                    break
                if (letter == '.'):
                    place = True
                if (place):
                    size += 1
                loc += 1
            if (size > 0):
                place_loc.append([loc, size])
        return place_loc
    
    compact_line = new_line[:]
    nb = 0
    for file in reversed(file_size):
        print(nb,"/",len(file_size))
        nb += 1
        find = False
        place_loc = get_loc()
        for place in place_loc:
            if (place[1] >= file[1] and place[0] - place[1] < file[2]):
                for i in range(file[1]):
                    compact_line[i + place[0] - place[1]] = str(file[0])
                    compact_line[i + file[2]] = '.'
                find = True
                break
    
    sum = 0
    mult = 0
    for letter in compact_line:
        if (letter == '.'):
            mult += 1
            continue
        sum += mult * int(letter)
        mult += 1
    print(line)
    print(new_line)
    print(compact_line)
    print(file_size)
    print(sum)


gold(line)
