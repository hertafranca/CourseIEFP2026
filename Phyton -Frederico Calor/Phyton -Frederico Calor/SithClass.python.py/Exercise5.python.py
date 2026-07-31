
#Crie um programa que introduza um array e faça a soma, colocar ao contrário e contar os números pares que estão no array:
     
numbers=[4,5,10,11,20,21]

reversed_numbers=numbers[::-1]
print("O inverso da ordem dos números do array é:",reversed_numbers)
soma=sum(numbers)
#addition=(int(4)+int(5)+int(10)+int(11)+int(20)+int(21))
print("A soma do array é:",soma)

#print("A soma de todos os números do array é:",addition)

for number in numbers:
    
    if number % 2 ==0 :
        print("Esse número é par:",number)
    











    
    