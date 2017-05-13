# Parité dans les investitures

Chacun des partis a un tableau récapitulatif avec les candidats investis, leur genre, et le score de leur candidat à la présidentielle.

## Comment lire le grand tableau

Les colonnes B à F représentent la séquence hommes / femmes chez les candidats des partis EM, FI, LR, FN et PS, selon le score décroissant du candidat présidentiel associé au premier tour.

Exemple : les trois premiers genres dans la séquence EM sont `H`,`H`,`H` parce que les candidats dans les circonscriptions les plus favorables à Macron sont trois hommes. (En l'occurence, Frédéric PETIT dans la 7è circo des Français de l'Étranger, Rolland LESCURE dans la 1è circo des Français de l'Étranger, et Benjamin GRIVEAUX dans la 5è circo de Paris.)

Les colonnes G à K représentent le nombre de `F` dans la séquence compté jusqu'à présent, pour chacun des partis.

Les colonnes L à P divisent les scores des colonnes G à K par le nombre de circonscriptions analysées.

Le même principe vaut pour `parite-simulations.csv`, sauf qu'à la place des 5 partis ce sont les 4 scénarios de simulation.