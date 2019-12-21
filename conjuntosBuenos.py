from sys import stdin, stdout

casos = int(stdin.readline())
numeros = [int(x) for x in stdin.readline().split()]
if casos < 2:
    stdout.write("false")
else:
    suma = numeros[0] % numeros[1] if numeros[0] > numeros[1] else numeros[1] % numeros[0]

    for x in xrange(1, casos-1):
        suma += numeros[x] % numeros[x + 1] if numeros[x] > numeros[x + 1] else numeros[x + 1] % numeros[x]
    
    if numeros[casos - 1] > suma:
        stdout.write("True")
    elif suma % numeros[casos - 1] == 1:
        stdout.write("False")
    else:
        stdout.write("True")
