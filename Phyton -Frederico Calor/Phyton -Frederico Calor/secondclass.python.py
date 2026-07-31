#"Calcule a sua idade baseada no ano que você nasceu e diga se é de maior ou de menor idade:"

birthYear=int(input("Qual seu ano de nascimento?"))
currentYear=int(input("Qual o ano atual?"))
currentAge=currentYear - birthYear

print(" Sua idade é:", currentAge)

if currentAge >= 18:
    print("Possue maior idade")
elif currentAge <= 13:
    print("Possue menor idade")
