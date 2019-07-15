# Violence Data Analisis

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA as sklearnPCA
from dateutil import parser
import unidecode


# create series with years of available data
start_year = 2001
end_year = 2019
years = np.arange(start_year,end_year,1)
# number of pages that correspond to each year in excel file
nop = [6]*(end_year - start_year)
# numper of pages processed.
count = 0	

raw_data = pd.DataFrame()

#import data page by page per year
loc ='data/Respuesta Solicitud  1893 lesionados por munis mensual y sexo de 2001 a 2017.xlsx' 
for (pages,year) in zip(nop,years):

	print("Leyendo ano: "+str(year))
	year_rdata = pd.DataFrame()

	for i in range(pages):

		#if its first page, skip row 1
		print("Pagina: "+str(count+i))
		if(i == 0):
			raw1 = pd.read_excel(loc, sheet_name = count + i, skiprows= 1)
		else:
			raw1 = pd.read_excel(loc, sheet_name = count + i)

		# clean columns
		#raw1 = raw1.dropna(how='all', axis = 0, thresh = 2)
		#raw1 = raw1[ ~raw1.loc[:,:].isnull() ]

		# Asignar nombres de departamento a municipios que no tienen
		raw1['MUNICIPIOS'] = raw1['MUNICIPIOS'].fillna(method='ffill')
		# Reasignar nombres de columna correctos. Utilizar nombres en ingles para posterior uso
		# en librerias
		columns = ['departamento', 'municipio','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','total1','t','man','woman','total2' ]
		raw1.columns = columns
		# eliminar columnas sin informacion o no utiles ahora
		raw1 = raw1.drop(columns=['total1','t','man','woman','total2'])
		
		# crear multi index list
		deps = list()
		muns = list()

		raw1['municipio'] = raw1['municipio'].apply(lambda x: unidecode.unidecode(x))
		raw1['departamento'] = raw1['departamento'].apply(lambda x: unidecode.unidecode(x))


		# create array with multiple indexes
		mi_array = list(zip(raw1['departamento'],raw1['municipio']))
		# create multiindex itself
		mi_index = pd.MultiIndex.from_tuples(mi_array, names=['departamento', 'municipio'])
		#mi_index = mi_index.dropna(how='any')

		# Transponer matriz para que el indice sean fechas (y coincida con otra data)
		raw1 = raw1.T
		raw1.index.name = 'months'
		# asignar nuevo multiindice
		raw1.columns = mi_index
		# eliminar filas que no sirven
		raw1 = raw1.drop(index ='departamento')
		raw1 = raw1.drop(index = 'municipio')

		# eliminar indexado por 'meses', este agrega una columna 'meses' al dataframe
		# con la misma informacion que el index
		raw1 = raw1.reset_index()

		# si no es la primer pagina de este ano, eliminar la columna de meses
		# para no anadir doble
		if (i != 0):
			raw1 = raw1.drop(columns = ['months'])

		# crear el dataframe final luego de importar el primer grupo de datos
		if( i == 0):
			year_rdata = raw1
		else:
			# concatenar o anexar a la par los datos del mismo ano por que
			# corresponden al mismo departamento
			year_rdata = pd.concat([year_rdata,raw1],  axis=1 ) #raw_data.append(raw1, ignore_index=True)



	# asignar ano de esta data
	year_rdata['year'] = year

	# add latest processed year to the main dataframe
	if(count == 0):
		raw_data = year_rdata
		print("Dimensiones de dataframe: "+str(raw_data.shape))
		print("Ano: {}".format(year_rdata['year'][:5]))
	else:
		print("Ano: {}".format(year_rdata['year'][:5]))
		try:
			raw_data = pd.concat([raw_data,year_rdata], ignore_index=True)
			print("Dimensiones de dataframe: "+str(raw_data.shape))
		except:
			print(raw_data.columns)
			print(year_rdata.columns)
			print( raw_data.columns == year_rdata.columns)
			raise ValueError('No son iguales los indices')

	print ("Se anadieron: "+str(i+1)+" paginas")
	count = count + i + 1


# convertir ano y mes a objeto datetime y asignar como indice del dataframe
raw_data['fecha'] = list(map(lambda x,y: parser.parse(str(x)+"-"+y+"-01"),raw_data['year'],raw_data['months']))
raw_data = raw_data.set_index('fecha')
#raw_data = raw_data.drop(columns=['fecha'])

# generar generador de excel
save_dir = 'data/Normalizado.xlsx'
writer = pd.ExcelWriter(save_dir)
raw_data.to_excel(writer,'Sheet1')
writer.save()
print("Saved file in {}".format(save_dir))

#graficar datos por departamento
for dep in np.unique(raw_data.columns.get_level_values('departamento')):
	#print("Depto: "+dep)
	a = raw_data.xs(dep, level='departamento', axis=1).columns.get_level_values('municipio')
	print("Depto: "+dep+" hay "+str(len(a))+" municipios")
	for mun in a:
		#print("   - "+mun)
		continue
	#print(dep)
	try:
		raw_data.xs(dep, level='departamento', axis=1).plot()
		continue
	except:
		print("No existe depto: "+dep)

#print(raw_data.head(5))
#print(raw_data.columns)
#print(raw_data.index)

#plt.show()
