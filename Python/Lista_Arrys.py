#Desenvolvimento Extra 1.4
#fazendo a troca via input
lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

def arrays():
  alterar = True
  cont = 0
  print("Esses são os nossos itens à venda!!!\n")

  for i in range(len(lista_produtos)):
    print("Temos", lista_produtos[i], "á venda")

  print("\nGostaria de  fazer alguma alteração?\nDigite 1 troca de produto\nDigite 2 para adicionar um produto\nDigite 3 para remover um produto\nDigite 0 para sair")
  while (alterar == True):

      comando = input()

      if (comando == '1' or comando == 's' or comando == 'S'):
        alterar = True

        print("Qual item deseja alterar?")
        for i in range(len(lista_produtos)):
          print(i, "-", lista_produtos[i])

        produto_alterar = int(input())

        print("Qual o nome do novo produto?")
        produto_novo = input()
        cont = cont + 1

        lista_produtos.pop(produto_alterar)
        lista_produtos.insert(produto_alterar,produto_novo)

        for i in range(len(lista_produtos)):

          print("Temos", lista_produtos[i], "á venda")

        print("\nGostaria de  fazer mais alguma alteração?\nDigite 1 troca de produto\nDigite 2 para adicionar um produto\nDigite 3 para remover um produto\nDigite 0 para sair")

      if (comando =='2'):
        print("Qual item deseja cadastrar?")

        produto_add = str(input())
        lista_produtos.append(produto_add)

        for i in range(len(lista_produtos)):

          print("Temos", lista_produtos[i], "á venda")
        print("\nGostaria de  fazer mais alguma alteração?\nDigite 1 troca de produto\nDigite 2 para adicionar um produto\nDigite 3 para remover um produto\nDigite 0 para sair")
        cont = cont + 1

      if (comando =='3'):
        print("Qual item deseja remover?")
        for i in range(len(lista_produtos)):
          print(i, "-", lista_produtos[i])

        produto_remover = int(input())
        lista_produtos.pop(produto_remover)

        for i in range(len(lista_produtos)):

          print("Temos", lista_produtos[i], "á venda")
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
  return

arrays()
