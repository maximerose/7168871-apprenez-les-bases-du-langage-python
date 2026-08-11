nombre1 = input("Entrez un nombre entier: ")
nombre2 = input("Entrez un nombre entier: ")


if not nombre1.isnumeric() or not nombre2.isnumeric():
  print("Erreur : les nombres saisis doivent être des entiers")
  raise SystemExit("Fin du programme")

nombre1 = int(nombre1)
nombre2 = int(nombre2)

operateur = input("Entrez l'opérateur (+, -, *, /): ")

if operateur not in ['+', '-', '*', '/']:
  print("Erreur : L'opérateur n'est pas reconnu")
  raise SystemExit("Fin du programme")

result = ''
match operateur:
  case '+':
    result = nombre1 + nombre2
  case '-':
    result = nombre1 - nombre2
  case '*':
    result = nombre1 * nombre2
  case '/':
    if nombre2 == 0:
      print("Erreur : Impossible de diviser par 0")
      raise SystemExit("Fin du programme")
    result = round(nombre1 / nombre2, 2)

print(f"Résultat: {result}")