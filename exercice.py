# ici le resultat de l'exercice
# 1 - Lire le fichier data.txt
# 2 - calculer la somme des données
# 3 - Enregistrer le resultat dans un fichier result.txt
# Bon courage

f = open("data.txt")
data_str = f.read()
print(f"contenu {data_str}")

data = [int(x) for x in data_str.split(',')]

#Calculer la somme
s = 0
for x in data: s+= x

# fermer le ficher en lecture
f.close()

#Ouvrir le fichier result.txt en ecriture
f = open("result.txt", "wt")

#Enregistrer la somme
f.write(str(s))

#Fermer le fichier
f.close()