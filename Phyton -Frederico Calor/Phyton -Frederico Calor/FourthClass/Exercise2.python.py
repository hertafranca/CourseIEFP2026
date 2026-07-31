

#Criar um programa que diga se o número é par ou se ele é impar(resto da divisão %)

number=int(input("Digite um número:"))
result=number % 2 
#print("O número {}". format(result))

if result == 0:
    print("Esse número é par")
else :
    print("Esse número é impar")
    