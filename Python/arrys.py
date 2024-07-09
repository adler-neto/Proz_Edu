#ex: utilizando arrys
lista_floats = [0.3, 3.9, 89.15, 123.45]
lista_strings = ["Eu", "gosto", "de", "panquecas"]
lista_booleanos = [False, True, True, False]
lista_listas = [[1, 2, 3], ['a', 'b', 'c']]
lista_mista = [10, 'dez', True]

print(lista_floats)
print(lista_strings)
print(lista_booleanos)
print(lista_listas)
print(lista_mista)

#indices
lista_frutas = ['maçã', 'banana', 'pera']
print(lista_frutas)

# Imprimirá: ['maçã', 'banana', 'pera']

# 'maçã' tem o índice 0
# 'banana' tem o índice 1
# 'pera' tem o índice 2

print(lista_frutas[0])
# Imprimirá: 'maçã'

lista_frutas = ['maçã', 'banana', 'pera']
fruta_preferida = lista_frutas[2]

print(fruta_preferida)
print(lista_frutas)

# O primeiro print() imprimirá: 'pera'
# O segundo print() imprimirá: ['maçã', 'banana', 'pera']

#comando len() a função len(), do inglês length (cumprimento), nos permite saber a quantidade de itens 
# num array, # basta passar o nome da variável que guarda o array como argumento.
lista_frutas = ['maçã', 'banana', 'pera']
quantidade_frutas = len(lista_frutas)

print(quantidade_frutas)

# Imprimirá o número 3, pois lista_frutas tem três elementos
#É possível também passar a função len() como argumento da função print(), 
#em guardar ela previamente numa variável:
print(len(lista_frutas))

loja_de_construcao = ["Cimento","Tijolo","Areia","Vergalhão","Enxada"]
ano_nascimento_irmaos = [1986,1987,1992,1994,1998]

print("Materiais disponíveis:")
for material in loja_de_construcao:
  print(loja_de_construcao.index(material)+1," - ", material)

print("Ano de nascimento entre irmãos:")
for ano in ano_nascimento_irmaos:
  print(ano_nascimento_irmaos.index(ano)+1," - ", ano)
  
  lista_frutas = ['maçã', 'banana', 'pera']
#atribuindo o tamanho da lista para x
x =len(lista_frutas)

for i in range(x):
    print(lista_frutas[i])
    
# Imprimirá:
# maçã
# banana
# pera

lista_num = [2, 45, 65, 78, 126, 987, 457, 345, 679, 107, 2345, 452, 3, 34, 560]
x = len(lista_num)
print("-----------------",x ,"-----------------")
for i in range(x):
    print(lista_num[i])
    
print("Total de ", x, "itens")

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

for indice_produto in range(len(lista_produtos)):
  print("Temos",lista_produtos[indice_produto],"à venda!")
  
  
  lista_frutas = ['melancia', 'morango', 'abacaxi']
print(lista_frutas)
# Imprimirá: ['melancia', 'morango', 'abacaxi']

# a função append(), que em inglês significa “anexar” ou “acrescentar” adiciona o elemento 
# passado como argumento no final
lista_frutas.append('kiwi')
print(lista_frutas)
# Imprimirá: ['melancia', 'morango', 'abacaxi', 'kiwi']

lista_frutas = ['melancia', 'morango', 'abacaxi', 'kiwi']
print(lista_frutas)
# Imprimirá: ['melancia', 'morango', 'abacaxi', 'kiwi']

#A função pop() vem para nos ajudar a resolver esse problema. Usamos ele da mesma forma que 
# a função append(), porém, não precisamos passar nenhum argumento dentro dos parênteses. 
# Assim, ele entenderá que o item a ser removido do array é o último.
lista_frutas.pop()
print(lista_frutas)
# Imprimirá: ['melancia', 'morango', 'abacaxi']