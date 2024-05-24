""""
Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

Escreva um código que imprima todos os números exceto o número 13.
Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.

Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

"""

#for crescente
for i in range (1,21,1):
    if (i == 13):
       continue
    print ("Andar ",i)  
 
print("------------------------------------")

#for decrescente

for i in range (20,0,-1):
    if (i == 13):
       continue
    print ("Andar ",i) 
   
print("------------------------------------")

# while crescente    
 
i = 1
while i < 21:
  if i == 13:
    i+=1
  print("Andar ", i)
  i += 1
  
print("------------------------------------")

# while decrescente    
 
i = 20
while i > 0:
  if i == 13:
    i-=1
  print("Andar ", i)
  i -= 1