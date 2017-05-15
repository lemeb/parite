from pandas import DataFrame as df

emdf = df.from_csv('../parite-em.csv').sort_values('MACRON', ascending=0)
lfidf = df.from_csv('../parite-lfi.csv').sort_values('MÉLENCHON', ascending=0)
fillondf = df.from_csv('../parite-lr.csv').sort_values('FILLON', ascending=0)
lependf = df.from_csv('../parite-fn.csv').sort_values('LE PEN', ascending=0)
hamondf = df.from_csv('../parite-ps.csv').sort_values('HAMON', ascending=0)

# Listes de genre

listes_genre = [list(emdf['genre']),
        list(lfidf['TG']),
        list(fillondf['genre']),
        list(lependf['genre']),
        list(hamondf['genre'])]

categories = ['H/F', 'NB f', 'Prop F']
headers = ['EM', 'LFI', 'LR', 'FN', 'PS']

# Calculs
listes_genre_et_counter = []
# Format = [
# ['H','F','F'etc.], (listes_genre)
# [0, 1, 2, etc.] (femmes_counter_array)
# [0.0, 0.5, 0.67, etc.] (proportion_counter)
# ]
for parti_liste in listes_genre:
    femmes_counter_array = []
    proportion_counter = []
    femmes_counter = 0
    for i in range(len(parti_liste)):
        if parti_liste[i] == 'F':
            femmes_counter += 1
        femmes_counter_array.append(femmes_counter)
        proportion_counter.append(femmes_counter / (i+1))
    listes_genre_et_counter.append((parti_liste, femmes_counter_array,proportion_counter))

partis_dfs = []
for i in range(len(listes_genre_et_counter)):
    parti_tableau = {}
    parti_grosses_listes = listes_genre_et_counter[i]
    for j in range(len(parti_grosses_listes)):
        categorie_liste = parti_grosses_listes[j]
        nom_colonne = (' '.join([categories[j],headers[i]]))
        parti_tableau[nom_colonne] = categorie_liste
    partis_dfs.append(df(parti_tableau))

import pandas as pd
t = pd.concat(partis_dfs, axis=1)
t['Classement des circonscriptions'] = range(1, len(l) + 1)
t.set_index('Classement des circonscriptions').to_csv('../gt.csv')
