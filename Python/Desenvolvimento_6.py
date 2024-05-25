"""
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
"""

def calc_idade():
    ano_anterior = 2021
    ano_atual = 2022
    
    nome_completo = input("Digite seu nome completo: ")    
    
    while True:

        data_nasc = input("Digite sua ano de nascimento! \nData de nascimento entre 1922 a 2021: ")

        if data_nasc.isdigit() and 1922 <= int(data_nasc) <= 2022:
            idade = ano_anterior - int(data_nasc)
            idade_atual = ano_atual - int(data_nasc)
            print("seu nome é:", nome_completo, "e a sua idade é:", idade)
            print("Você fara ", idade_atual, "no ano atual!")
            break
        else:
            print("Ano de nascimento invalido, digite ano entre 1922 e 2021")

calc_idade()
    