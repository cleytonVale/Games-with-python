print("************Calculadora************")

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

def soma(x, y):
    return x + y;

def subtracao(x, y):
    return x - y;

x = int(input("Digite o 1º numero: "))
y = int(input("Digite o 2º número: "))
escolha = input("Escolha o operador: (+) | (-) | (*) | (/): ")

if (escolha == "+"):
    print("O valor é = ", soma(x, y))
elif (escolha == "-"):
    print("o Valor é = ", subtracao(x, y))
elif (escolha == "/"):
    print("o Valor é = ", divisao(x, y))
elif (escolha == "*"):
    print("o Valor é = ", multiplicacao(x, y))
else:
    print("Entrada incorreta, Tente novamente")
