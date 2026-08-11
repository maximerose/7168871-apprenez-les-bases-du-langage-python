# Ecrivez votre code ici !
nombres = input("Entrez une liste de nombres entiers séparés par une virgule: ")
liste = nombres.split(',')
print(liste)

liste_entiers = [] 
for nombre in liste:
  nombre_entier = int(nombre)
  liste_entiers.append(nombre_entier)

somme = sum(liste_entiers)
print(f"Somme {somme}")
moyenne = round(sum(liste_entiers) / len(liste_entiers), 2)
print("Moyenne", moyenne)

nombre_sup_moyenne = 0

for nombre in liste_entiers:
  if nombre > moyenne:
    nombre_sup_moyenne += 1


print(f"Nombres supérieurs à la moyenne : {nombre_sup_moyenne}")