


chaine = input("Veuillez entrer une chaîne de caractères : ")


if len(chaine) < 10:
    print("Chaîne pas assez longue")
elif len(chaine) > 10:
    print("Chaîne trop longue")
else:
    print("Chaîne parfaite")

    
    print("Premier caractère :", chaine[0])
    print("Dernier caractère :", chaine[-1])

   