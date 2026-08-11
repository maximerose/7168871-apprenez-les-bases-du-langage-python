def get_salaire_mensuel(salaire_annuel):
  return round(float(salaire_annuel) / 12, 2)

def get_salaire_hebdomadaire(salaire_mensuel):
  return round(float(salaire_mensuel) / 4, 2)

def get_salaire_horaire(salaire_hebdomadaire, heures_travaillees):
  return round(float(salaire_hebdomadaire) / float(heures_travaillees), 2)

salaire_annuel = input("Entrez votre salaire annuel: ")
while not salaire_annuel.isnumeric():
  print("Erreur : ce n'est pas un nombre")
  salaire_annuel = input("Entrez votre salaire annuel: ")

nb_heures_hebdo = input("Combien d'heures travaillez-vous par semaine ? ")
while not nb_heures_hebdo.isnumeric():
  print("Erreur : ce n'est pas un nombre")
  nb_heures_hebdo = input("Combien d'heures travaillez-vous par semaine ? ")

salaire = get_salaire_horaire(get_salaire_hebdomadaire(get_salaire_mensuel(salaire_annuel)), nb_heures_hebdo)
print(f"Votre salaire horaire est de {salaire} euros")

