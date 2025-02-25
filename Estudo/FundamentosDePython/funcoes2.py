fluxo_caixa = []

print("-------------------")
print("Fluxo de Caixa")
print("-------------------")
print("1 - Adicionar Receita")
print("2 - Adicionar Despesa")
print("\n# Digite 'sair' para encerrar o programa #\n")

def adicionar_trans():
    nome = input("Nome: ")
    valor = float(input("Valor: "))
    fluxo_caixa.append({
        "nome": nome,
        "valor": valor
        })

while True:
    opcao = input("Selecione uma opção: ")
    
    if opcao == "1":
        adicionar_trans()
    elif opcao == "2":
        adicionar_trans()
    elif opcao.lower() == "sair":
        break
    
    total = 0
    for fc in fluxo_caixa:
        print("Nome: ", fc["nome"], ", VALOR: R$", fc["valor"])
        total += fc["valor"]
        
    print("Total em caixa: R$", total)