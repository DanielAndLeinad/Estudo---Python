def minha_funcao(valor1, valor2):
    return valor1 + valor2

resp = minha_funcao(10, 20)
print(resp)

def minha_funcao2(valor1, valor2):
    return valor1 + valor2

while True:
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    resp = minha_funcao2(valor1, valor2)
    print(resp)
    if valor1 == 0 or valor2 == 0:
        break