from tabulate import tabulate

data = [
       ["Alice",25, "Estudante"],
       ["Bob", 27, "Dev"]
       ]

tabela_formatada = tabulate(data, headers=["Nome", "Idade", "Profissão"])

print(tabela_formatada)
    