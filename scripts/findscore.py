from pandas import DataFrame as df

psdf = df.from_csv('data/p17_seulement_scrutins.csv').reset_index()

def makenewdf(candidat):
	newdf = psdf[['code_circo', 'Exprimés',candidat]]
	newdf[candidat] = newdf[candidat] / newdf['Exprimés']
	newdf = newdf.drop('Exprimés', axis=1).set_index('code_circo')
	return newdf

newdf = makenewdf('LE PEN')
lependf = df.from_csv('data/investitures-FN.csv')
lependf = lependf.drop(['circo', 'departement', 'site'], axis=1)
lependf.join(newdf).sort_values('LE PEN', ascending=0).to_csv('../parite-fn.csv')

newdf = makenewdf('FILLON')
fillondf = df.from_csv('data/investitures-republicains.csv')
fillondf.join(newdf).sort_values('FILLON', ascending=0).to_csv('../parite-lr.csv')

newdf = makenewdf('HAMON')
hamondf = df.from_csv('data/investitures-socialistes.csv')
hamondf = hamondf.drop(['dpt', 'circo'], axis=1).set_index('code_circo')
hamondf.join(newdf).sort_values('HAMON', ascending=0).to_csv('../parite-ps.csv')

newdf = makenewdf('MÉLENCHON')
lfidf = df.from_csv('data/investitures-lfi.csv')
lfidf.join(newdf).sort_values('MÉLENCHON', ascending=0).to_csv('../parite-lfi.csv')

newdf = makenewdf('MACRON')
emdf = df.from_csv('data/investitures-en-marche.csv').reset_index()
emdf = emdf.drop(['code_dpt', 'circo'], axis=1).set_index('code_circo')
emdf.join(newdf).sort_values('MACRON', ascending=0).to_csv('../parite-em.csv')
