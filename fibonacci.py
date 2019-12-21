from sys import stdin, stdout

x, y = 0, 1

for x in range(int(stdin.readline()) - 1):
    x, y = y, x + y

stdout.write(str(y))