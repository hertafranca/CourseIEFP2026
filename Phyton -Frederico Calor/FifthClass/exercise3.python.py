#Criar um programa que imprima todos os números pares de 1 a 500, usando o if dentro do while.

result = 1


while result <=500:
    
    
    if result % 2 !=0 :
        print("Esse número é ímpar:",result)
        
    else:
        print("Esse número é par:",result) 
        
    result= result + 1 # fora do if/else mas dentro do while