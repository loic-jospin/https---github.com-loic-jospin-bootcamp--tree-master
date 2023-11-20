number=int(input("entrer un nombre: "))
print(number)
info1=f"le nombre {number} est pair"
info2=f"le nombre {number} est impair"
if number % 2 ==0:
    print(info1)
else:
    print(info2)