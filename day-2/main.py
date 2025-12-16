print("########## Bienvenue sur le calculateur de pourboires !   ##########")

# poser la question aux clients

price = float(input("Quel est le montant total de la facture ? \n $:"))

percent = float(input("Quel montant de pourboire souhaitez-vous donner ? \n Percent : "))

people = int(input("Combien de personnes pour partager l'addition ? \n People :"))

# calcul

result =(((price * (percent / 100)) + price) / people)

# affichage de la somme que chaque personne doit verser

print(f"Chaque personne doit payer : {result:.2f}")