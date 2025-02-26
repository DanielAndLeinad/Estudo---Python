salario = float(input("Qual seu salario?: "))
if salario >= 1000:
    print("programador junior")
elif salario >= 3000 and salario <= 5000:
    print("programador pleno")
elif salario >= 5000 and salario <= 10000:
    print("programador senior")
else:
    print("gerente de projeto")