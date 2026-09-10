aluno_nota1 = float(input('Insira a primeira nota: ')) 

aluno_nota2 = float(input('Insira a segunda nota: ')) 

media = (aluno_nota1 +  aluno_nota2) / 2


if media < 6:
    print(f'Aluno reprovado, a nota do aluno foi {media} ')
elif media >= 6:
    print(f'Aluno aprovado, a nota do aluno foi {media} ')
