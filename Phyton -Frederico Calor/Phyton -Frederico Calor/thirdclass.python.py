#" Calcule as notas de um aluno, tire a média e diga se ele foi aprovado ou reprovado:"

student=(input("Digite o nome do aluno:"))
grade1=float(input("Digite a média do primeiro bimestre:"))
grade2=float(input("Digite a média do segundo bimestre:"))
grade3=float(input("Digite a média do terceiro bimestre:"))
grade4=float(input("Digite a média do quarto bimestre:"))

media=(grade1+grade2+grade3+grade4)/4

print("A média de",student,"é:",media)

if media >= 10.0 and media <15 : # aqui vai de 10 a 15(nao inclusivo)
    print("Parabéns",student,"você está Aprovada.")
elif media <= 9.9 and media > 5.0: # aqui vai entre o 9.9 ao 5  nao inclusivo
    print("Nâo atingiu a média.")
elif(media <= 5.0): # menor que 5
    print("es muito mau.")
else: # todos os que tiverem media superio a 15 
    print("O aluno ",student,"foi dos melhores")
    