'''


Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''

numero1 = float(input("Digite o número 1: "))
numero2 = float(input("Digite o número 2: "))
operacao = input("Digite a operação que deseja realizar: [+, -, /, *]: ")


def checar():
    if (resultado_operacao // 1 == resultado_operacao):
        print("o número é Inteiro")
        if resultado_operacao % 2 == 0:
            print("o número é Par")
            if resultado_operacao > 0:
                print("o número é Positivo")
            else:
                print("o número é Negativo")
        else:
            print("o número é Impar")
    else:
        print("o número é Decimal")


if operacao == '+':
    resultado_operacao = numero1 + numero2
    print("Resultado é: ", resultado_operacao)
    checar()
elif operacao == '-':
    resultado_operacao = numero1 - numero2
    print("O Resultado é: ", resultado_operacao)
    checar()
elif operacao == '/':
    resultado_operacao = numero1 / numero2
    print("O Resultado é: ", resultado_operacao)
    checar()
elif operacao == '*':
    resultado_operacao = numero1 * numero2
    print("O Resultado é: ", resultado_operacao)
    checar()
else:
    print("O Valor Invalido")