menu_titulos = ["nome tarefa ->","descrição tarefa ->","status da tarefa"]
lista_tarefas = ["lavar carro","limpeza casa"]
descricao_tarefas =["lavagem, apiração e secar o carro","varrer e passar pano e lavar as louças"]
status_tarefas =["pendente","concluído"]

alterar = True
cont = 0
print("Essas são sua listas de tarefas!!!\n")

for i in range(len(lista_tarefas)):
  print(menu_titulos[0],menu_titulos[1],menu_titulos[2])
  print(lista_tarefas[i], "->", descricao_tarefas[i],"->", status_tarefas[i])

print("\nGostaria de  fazer alguma alteração?\nDigite 1 alterar a tarefa\nDigite 2 para adicionar uma tarefa\nDigite 3 para remover uma tarefa\nDigite 0 para sair")
while (alterar == True):

      comando = input()

      if (comando == '1'):
        alterar = True

        print("Qual tarefa deseja alterar?")
        for i in range(len(lista_tarefas)):
          print(i, "-", lista_tarefas[i])

        produto_alterar = int(input())

        print("Qual o nome da nova tarefa?")
        produto_novo = input()
        cont = cont + 1

        lista_tarefas.pop(produto_alterar)
        lista_tarefas.insert(produto_alterar,produto_novo)

        for i in range(len(lista_tarefas)):

          print("Temos as seguinte listas de tarefas:", lista_tarefas[i])

        print("\nGostaria de  fazer mais alguma alteração?\nDigite 1 troca de produto\nDigite 2 para adicionar um produto\nDigite 3 para remover um produto\nDigite 0 para sair")

      if (comando =='2'):
        print("Qual tarefa deseja cadastrar?")

        produto_add = str(input())
        lista_tarefas.append(produto_add)

        for i in range(len(lista_tarefas)):

          print("Temos as seguinte listas de tarefas:", lista_tarefas[i])
        print("\nGostaria de  fazer mais alguma alteração?\nDigite 1 troca de produto\nDigite 2 para adicionar um produto\nDigite 3 para remover um produto\nDigite 0 para sair")
        cont = cont + 1

      if (comando =='3'):
        print("Qual tarefa deseja remover?")
        for i in range(len(lista_tarefas)):
          print(i, "-", lista_tarefas[i])

        produto_remover = int(input())
        lista_tarefas.pop(produto_remover)

        for i in range(len(lista_tarefas)):

          print("Temos as seguinte listas de tarefas:", lista_tarefas[i])
        print("\nGostaria de  fazer mais alguma alteração?\nDigite 1 troca de produto\nDigite 2 para adicionar um produto\nDigite 3 para remover um produto\nDigite 0 para sair")
        cont = cont + 1

      elif (comando == '0' or comando == 'n' or comando == 'N'):
        if (cont == 0):
          print("Você saiu sem fazer nenhuma alteração!!")
        elif (cont == 1):
          print("Alteração feita com sucesso!!")
        else:
          print("Alterações feita com sucesso!!")
        alterar = False