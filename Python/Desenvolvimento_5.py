"""
Instruções do projeto
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o 
usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem 
“Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar 
a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 
"""
def calc():
    
    while True:
        print("Digite a opção para o operador: \n 1 para soma; \n 2 para subtração; \n 3 para multiplicação; \n 4 para divisão; \n 0 para sair:")
        operacao = input()
    
        if operacao in ('1','2','3','4'):
            print("Digite o primeiro número: ")
            numero1 = float(input())
            print("Digite o segundo número: ")
            numero2 = float(input())
    
            if (operacao == '1'):
        # print("Você escolheu soma" )
                print("Resultado da soma é: ", numero1 + numero2)
            elif (operacao == '2'):
        #print("você escolheu a subitração")
                print("Resultao da subtração é: ", numero1 - numero2)
            elif(operacao == '3'):
        #print("Voccê escolheu multiplicação")
                print("Resultado da multiplicação é: ", numero1 * numero2)
            elif (operacao == '4') and (numero2 != 0):
        #print("Voce escolheu divisão")
                print("Resultado da divisão é: ", numero1 / numero2)         
            else:
                print("Resultado = 0")  
        elif operacao == '0':
            break
        else:
            print("Essa opçãonão existe,tente novamente!")
        
calc()