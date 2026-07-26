#Criar um programa que diga uma sequencia até 500 e defina cada número se é par ou ímpar:

number=0

while number <=500:
  #print("Antes:",number)
  typeNumber=number%2
  if typeNumber != 0:
    print("Esse número é ímpar:",number)
  else:
    print("Esse número é par:",number)
  number=number +1
  #print("Depois:",number)