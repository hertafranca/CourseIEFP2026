#Criar um programa que dentro de 3 nota busque a media de maior:


note1=["6","6","6"]
note2=["3","3","3"]
note3=["9","9","9"]

media1=float(note1[0])+float(note1[1])+float(note3[2])/3

media2=float(note2[0])+float(note2[1])+float(note2[2])/3

media3=float(note3[0])+float(note3[1])+float(note3[2])/3

#print("A média da primeira nota é:",media1)

#print("A média da segunda nota é:",media2)

#print("A média da terceira nota é:",media3


mediaMax=max(media1,media2,media3)

if mediaMax == media1:
    print(f"A maior média é a primeira: {media1}")
elif mediaMax == media2:
    print(f"A maior média é a segunda: {media2}")
else:
    print(f"A maior média é a terceira: {media3}")


        
        

