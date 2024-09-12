#opções de números e operações
def main():
    op = input("Digite a operação (+, -, *, /): ")
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))

    if op == '+':
        print(x + y)
    elif op == '-':
        print(x - y)
    elif op == '*':
        print(x * y)
    elif op == '/':
        if y != 0:
            print(x / y)
        else:
            print("Erro: Divisão por zero")
    else:
        print("Operação inválida")

if "_main_":
    main()