##
## PHYTON PROJECT, 2024
## main.py
## File description:
## You know, I don t think there are good or bad descriptions,
## for me, life is above all about functions...
##

from itertools import *
from math import *

lines = []
while True:
    line = input()
    if line.lower() == 's':
        break
    lines.append(line.split(":"))
    nbr_list = lines[-1][1].split()
    lines[-1].pop()
    for nbr in nbr_list:
        lines[-1].append(nbr)
    lines[-1] = list(map(lambda nbr: int(nbr), lines[-1]))

def eval_gd_s(res):
    res_split = res.split()
    resultat = int(res_split[0])

    for i in range(1, len(res_split), 2):
        op = res_split[i]
        next = int(res_split[i+1])
        
        if op == '+':
            resultat += next
        elif op == '*':
            resultat *= next
    return resultat

def silver(lines):
    sum = 0

    for line in lines:
        nombres = line[1:]
        operateurs = ['+', '*']
        combinaisons_operateurs = product(operateurs, repeat=len(nombres)-1)
        resultats = []
    
        for ops in combinaisons_operateurs:
            expression = str(nombres[0])
            for i, op in enumerate(ops):
                expression += f" {op} {nombres[i+1]}"
            resultats.append(expression)
        for res in resultats:
            if (eval_gd_s(res) == line[0]):
                sum += line[0]
                break
    print(sum)

def eval_gd_g(res):
    res_split = res.split()
    resultat = int(res_split[0])

    for i in range(1, len(res_split), 2):
        op = res_split[i]
        next = int(res_split[i + 1])
        
        if op == '+':
            resultat += next
        elif op == '*':
            resultat *= next
        elif op == '|':
            resultat = int(str(resultat) + str(next))
    return resultat

def gold(lines):
    sum = 0

    for line in lines:
        nombres = line[1:]
        operateurs = ['|', '+', '*']
        combinaisons_operateurs = product(operateurs, repeat=len(nombres)-1)
        resultats = []
    
        for ops in combinaisons_operateurs:
            expression = str(nombres[0])
            for i, op in enumerate(ops):
                expression += f" {op} {nombres[i+1]}"
            resultats.append(expression)
        for res in resultats:
            #print(res, eval_gd_g(res), line[0])
            if (eval_gd_g(res) == line[0]):
                sum += line[0]
                print(len(lines), lines.index(line), res, eval_gd_g(res), line[0])
                break
    print(sum)

gold(lines)
