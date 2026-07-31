#Criar um programa que de acordo com o número que foi introduzido pelo o usuário e mostre a sua sequência e ao mesmo tempo esses números estejam sendo somados:

number = int ( input(" Digita um número:"))
count=1
addition=0

while count <= number:
    print(count,end="")
    addition=addition + count
    
    if count < number:
        print("+",end="")
        count=count + 1
        
    print("=",addition)
    
        