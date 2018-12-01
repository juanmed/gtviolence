# Violence Data Analisis

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA as sklearnPCA

# create series with years of available data
years = np.arange(2001,2019,1)
# number of pages that correspond to each year in excel file
nop = [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5]
# numper of pages processed.
count = 0	


#import data page by page per year
loc ='data/Respuesta Solicitud  1893 lesionados por munis mensual y sexo de 2001 a 2017.xlsx' 
for (pages,year) in zip(nop,years):
	count2 = 0
	for i in range(pages):
		#if its first page, skip row 1
		if(i == 0)
			raw1 = pd.read_excel(loc, sheet_name = count + count2, skiprows= 1)
		else:
			raw1 = pd.read_excel(loc, sheet_name = 0, skiprows= 1)

		# otra pagina procesada
		count = count + 1

	count = count + count 2

raw1 = pd.read_excel(loc, sheet_name = 0, skiprows= 1)
# Asignar nombres de departamento a municipios que no tienen
raw1['MUNICIPIOS'] = raw1['MUNICIPIOS'].fillna(method='ffill')
# Reasignar nombres de columna correctos. Utilizar nombres en ingles para posterior uso
# en librerias
columns = ['departamento', 'municipio','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','total1','t','man','woman','total2' ]
raw1.columns = columns
# eliminar columnas sin informacion
raw1 = raw1.drop(columns='t')

# crear multi index list
deps = list()
muns = list()

# create array with multiple indexes
mi_array = list(zip(raw1['departamento'],raw1['municipio']))
# create multiindex itself
mi_index = pd.MultiIndex.from_tuples(mi_array, names=['departamento', 'municipio'])

# Transponer matriz para que el indice sean fechas (y coincida con otra data)
raw1 = raw1.T
raw1.index.name = 'meses'
# asignar nuevo multiindice
raw1.columns = mi_index
# eliminar filas que no sirven
raw1 = raw1.drop(index ='departamento')
raw1 = raw1.drop(index = 'municipio')
# asignar ano de esta data
raw1['year'] = 2001
# eliminar indexado por 'meses'
raw1 = raw1.reset_index()

print(raw1.head(5))
print(raw1.columns)
print(raw1.index)