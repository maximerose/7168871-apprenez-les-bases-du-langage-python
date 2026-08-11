fruits = {"pomme": "rouge", "banane": "jaune", "orange": "orange"}
print(fruits)
print("On ajoute kiwi : vert")
fruits["kiwi"] = "vert"
print(fruits)
couleur_banane = fruits["banane"]
print(f"couleur_banane: {couleur_banane}")
print("La pomme devient verte")
fruits["pomme"] = "vert"
print(fruits)
print("On supprime banane")
del fruits["banane"]
print(fruits)
print(f"Clés restantes: {fruits.keys()}")