from ctypes import sizeof


fruits = ["pomme", "banane", "orange"]
print(fruits)
print("On ajoute kiwi")
fruits.append("kiwi")
print(fruits)
print("On supprime orange")
fruits.remove("orange")
print(fruits)
print("On change le 2eme en ananas")
fruits[1] = "ananas"
print(fruits)
print(f"Longueur: {len(fruits)}")
print("On trie la liste dans l'ordre alphabétique")
fruits.sort()
print(fruits)

