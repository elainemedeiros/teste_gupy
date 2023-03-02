#Capturando o número informado pelo usuário
numero = int(input("Digite um número: "))

#Iniciando as variáveis
x, y = 0, 1

#Calculando se o número pertence à sequência de Fibonacci
while y < numero:
    x, y = y, x + y
if numero == 0:
    print("O número", numero, "pertence à sequência de Fibonacci")
else:
    if y == numero:
        print("O número", numero, "pertence à sequência de Fibonacci")
    else:
         print("O número", numero, "não pertence à sequência de Fibonacci")