
# Crie um programa que diga a classificação de um indivíduo de acordo com a sua idade:

classAge= int(input("Quantos anos você possue?"))

if  classAge in range (0,4):
    print("Foi classificado como Baby")

elif classAge in range (5,13):
    print("Foi classificado como child")
    
elif classAge in range (14,18):
    print("Foi classificado como teen")
    
elif classAge in range (16,65):
    print("Foi classificado como adult")
    
elif classAge in range (65, 100):
    print("Foi classificado como old")
    
else:
    print("Parabéns, Classificação STRONG")

