from difflib import get_close_matches
from pandas import DataFrame as df

candidat = 'HAMON'
psdf = df.from_csv('data/p17_seulement_scrutins.csv').reset_index()
newdf = psdf[['code_circo', 'Exprimés',candidat]]
newdf[candidat] = newdf[candidat] / newdf['Exprimés']
newdf = newdf.drop('Exprimés', axis=1).set_index('code_circo')

lependf = df.from_csv('data/investitures-FN.csv')
lependf = lependf.drop(['circo', 'departement', 'site'], axis=1)
lependf.join(newdf).to_csv('../lepen_circ.csv')

fillondf = df.from_csv('data/investitures-republicains.csv')
fillondf.join(newdf).to_csv('../fillon_circ.csv')

hamondf = df.from_csv('data/investitures-socialistes.csv')
hamondf = hamondf.drop(['dpt', 'circo'], axis=1).set_index('code_circo')
hamondf.join(newdf).to_csv('../hamon_circ.csv')
