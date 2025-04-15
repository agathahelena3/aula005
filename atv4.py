alunos = int(input("Digite o número de alunos:"))

i = 1
nota = 0
soma = 0
media = 0

while i <= alunos:
    nota = int(input(f"Digite a nota do aluno {i}:"))
    i = i+1
    soma = soma + nota

media = soma /alunos

print (f"A média da turma é {media}.")