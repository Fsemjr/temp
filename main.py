print('Seu triangulo e tipos')

#variaveis
a = float(input('Lado A:  '))
b = float(input('Lado B:  '))
c = float(input('Lado C:  '))

#teste dos triangulos

if (a + b < c) or (a + c < b) or (b + c < a):
        print('Nao é um triangulo')
elif (a == b) and (a == c):
        print('Equilatero')
elif (a==b) or (a==c) or (b==c):
        print('Isósceles')
else:
        print('Escaleno')