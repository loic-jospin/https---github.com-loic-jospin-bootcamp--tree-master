
taille_pouces = float(input("Veuillez entrer votre taille en pouces : "))

taille_cm = taille_pouces * 2.54
print(taille_cm)
if taille_cm > 145:
    print("Vous êtes assez grand pour rouler !")
else:
    print("Vous devez encore grandir pour pouvoir rouler.")
