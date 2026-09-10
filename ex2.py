num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
num3 = float(input('Digite o terceiro numero: '))

lista_numeros = [num1, num2, num3]

maior_numero = 0
if num1 == num2 and num2 == num3:
    print('Os numeros são iguais')

if num1 != num2 and num3:
    for i in lista_numeros:
        if i > maior_numero:
            maior_numero = i
    print(f'O maior numero é o numero: {maior_numero} ')