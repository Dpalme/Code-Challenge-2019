from sys import stdin, stdout

numDigitos = stdin.readline().split()[0]
digitos = len(numDigitos)
num = int(numDigitos)
potencia = (10 ** (digitos - 1))
suma = ((num-potencia) * digitos) + digitos

for x in xrange(digitos-1):
    suma += 9 * (10 ** x) * (x + 1)

stdout.write(str(suma))
