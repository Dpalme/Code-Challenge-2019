from sys import stdin, stdout

Topos = {}
Repetidos = []
stdin.readline()
for topo in [int(x) for x in stdin.readline().split()]:
    try:
        Topos[topo] += 1
        if Repetidos.index(topo) == -1:
            Repetidos.append(topo)
    except KeyError:
        Topos[topo] = 0

for i in Repetidos:
    stdout.write(str(i) + " ")
