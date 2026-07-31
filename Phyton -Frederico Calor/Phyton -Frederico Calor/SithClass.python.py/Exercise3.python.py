#Crie um array e diga quantos nomes queres introduzir:

names= [] 
people=int(input("Quantos nomes queres introduzir?"))

for i in range (people):
    newName=input(F"Digite o {i+1}ºnames:")
    names.append(newName)
    
    
for name in names:
    print(name)

