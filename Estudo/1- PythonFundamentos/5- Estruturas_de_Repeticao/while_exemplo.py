notas = []

contador = 1
while contador <= 5:
    codigo_aluno = input("Digite o código do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    contador += 1
print("Quantidade de notas: ", len(notas))