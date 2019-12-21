from sys import stdin, stdout, exit
from math import sqrt


def distancia(pos1, pos2):
    return sqrt(((pos2[0] - pos1[0]) ** 2) + ((pos2[1] - pos1[1]) ** 2))

meta = [int(coord) for coord in stdin.readline().split()]
stdin.readline()
distCoraje = distancia([0,0], meta)

for fantasma in stdin.readlines():
    posFantasma = [int(x) for x in fantasma.split()]
    if distancia(meta, posFantasma) <= distCoraje:
        break
else:
    stdout.write("false")
    exit(1)
stdout.write("true")