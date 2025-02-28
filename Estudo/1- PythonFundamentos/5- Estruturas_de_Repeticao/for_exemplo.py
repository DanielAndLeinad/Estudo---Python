notas = []
for x in range(5):
    codigo_aluno = input("Digite o código do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)  
print("Quantidade de notas: ", len(notas))
for n in notas:
    print("O aluno", n[0], "tirou a nota", n[1])   