"""
Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e 
o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:

1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
"""
def calc (numero1,numero2,operacao):
    if (operacao ==1):
        resultado = numero1 + numero2
    elif(operacao ==2):
        resultado = numero1 - numero2
    elif(operacao ==3):
        resultado = numero1 * numero2
    elif(operacao ==4) and (numero2!= 0):
        resultado = numero1 / numero2
    else:
        resultado = 0
    return resultado


resultado = calc(5,3,1)
print("O resultado é :", resultado)

resultado = calc(5,3,2)
print("O resultado é:", resultado)

resultado = calc(5,3,3)
print("O resultado é :", resultado)

resultado = calc(5,3,4)
print("O resultado é :", resultado)

reaultado = calc(5,3,6)
print("O resultado é :", reaultado)