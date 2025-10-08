print("------------Calculadora----------")

n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))

resultado = n1 + n2
print("A soma é:", resultado)

resultado = n1 * n2
print("A multiplicação é:", resultado)

resultado = n1 - n2
print("A subtração é:", resultado)

if n2 != 0:
    resultado = n1 / n2
    print("A divisão é:", resultado)
else:
    print("Não é possível dividir por zero!")
