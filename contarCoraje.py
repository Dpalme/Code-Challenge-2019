from sys import stdin, stdout

for x in xrange(int(stdin.readline())):
    stdout.write(str(int(stdin.readline()) % 6) + '\n')