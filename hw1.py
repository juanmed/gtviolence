import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA as sklearnPCA



import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls

# get color map from data list
def getColorMap(data):
	cmap = plt.get_cmap(name) # Get desired colormap - you can change this!
	max_height = np.max(data)   # get range of colorbars so we can normalize
	min_height = np.min(data)
	# scale each z to [0,1], and get their rgb values
	rgba = [cmap(((k-min_height)/max_height) ) for k in data] 
	#rgba = [cmap(1.0 - ((k-min_height)/max_height) ) for k in data] 
	return rgba


#import gt murder data
ymd = pd.read_excel('gtdata/gtym.xlsx' )
ymd = ymd.groupby("dpto").sum()
ymd.columns = [str(x) for x in np.arange(2001,2018,1)]
# transpose data for it to be indexed by year
ymd = ymd.T
#print (len(ymd.index.values))

#import weather data
# columns = Year	Month	Day	Hour	Minute	
#			DHI	DNI	GHI	Wind Speed	Precipitable Water	
#			Relative Humidity	Temperature

a = [str(x)+".csv" for x in np.arange(2001,2018,1)]
w = 0
for (i,filename) in enumerate (a):
	path = 'wdata/'+filename
	b = pd.read_csv(path, skiprows = 2)
	b = b.groupby('Year').mean()
	if i == 0:
		w = b
	else:
		w = w.append(b)

#print(len(w.index.values))

# force same index to correct types
ymd.index = w.index
#ymd.plot(y = 'Guatemala', title = 'Total Homicides per Year', color = 'b')

#plot some weather data
#w.plot( y = 'Temperature', title = "Temperature {C}", color = 'r')
#w.plot( y = 'Relative Humidity', title = "Relative Humidity {%}", color = 'b')
#w.plot( y = 'Precipitable Water' , title = "Precipitable Water {cm}" , color = 'g')
#w.plot( y = 'Wind Speed', title = "Wind Speed {m/s}" , color = 'm')
#w.plot( y = 'DNI', title = "Direct Normal Irradiance {w/m2}" , color = 'c')
#w.plot( y = 'DHI', title = "Direct Horizontal Irradiance {w/m2}" , color = 'y')
#w.plot( y = 'GHI', title = "Global Horizonal Irradiance {w/m2}" , color = 'k')


# create dataframe for Guatemala City
gtcity = pd.DataFrame()
gtcity['homicide'] = ymd['Guatemala']
gtcity['Temperature'] = w['Temperature']
gtcity['Precipitable Water'] = w['Precipitable Water']
gtcity['Wind Speed'] = w['Wind Speed']
gtcity['DNI'] = w['DNI']
gtcity['DHI'] = w['DHI']
gtcity['GHI'] = w['GHI']
gtcity = gtcity.sort_values(by = 'homicide')


#gtcity.plot(kind = 'scatter', x = 'Temperature', y= 'homicide', color = 'r', title = "Homicides vs Temperature {C}")
#gtcity.plot(kind = 'scatter',x = 'Precipitable Water', y= 'homicide', color = 'g', title = "Homicides vs Precipitable Water {cm}")
#gtcity.plot(kind = 'scatter',x = 'Wind Speed', y= 'homicide', color = 'm', title = "Homicides vs Wind Speed {m/s}")
#gtcity.plot(kind = 'scatter',x = 'DNI', y= 'homicide', color = 'c', title = "Homicides vs DNI {w/m2}")
#gtcity.plot(kind = 'scatter',x = 'DHI', y= 'homicide', color = 'y', title = "Homicides vs DHI {w/m2}")
#gtcity.plot(kind = 'scatter',x = 'GHI', y= 'homicide', color = 'k', title = "Homicides vs GHI {w/m2}")

#cov = gtcity.cov()
#cov = cov.at[:,:].values
#cov.to_clipboard(sep=",	")

# get only values
data = gtcity.iloc[:,1:].values
# get only murder data
y = gtcity.iloc[:,0].values

# standardize data
data_std = data # StandardScaler().fit_transform(data)
# get covariance matrix, pass transpose of data because that is what np.cov expects
cov = np.cov(data.T)
# get eigen values and vectors
eig_vals, eig_vecs = np.linalg.eig(cov)
#print('Eigen Values {}'.format(eig_vals))
#print('Eigen Vectors {}'.format(eig_vecs))

# Make a list of (eigenvalue, eigenvector) tuples
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]

# Sort the (eigenvalue, eigenvector) tuples from high to low
eig_pairs.sort()
eig_pairs.reverse()
#print('Eigen values in descending order:')
#for pair in eig_pairs:
#	print(pair[0])

# Draw information 
tot = sum(eig_vals)
var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)
#print(cum_var_exp)

fig = plt.figure()
"""
ax = fig.add_subplot(1,1,1)
ax.plot(['PC %s' %i for i in range(0,len(var_exp))], cum_var_exp, color='m', label = "Cumulative Explained Variance" )
ax.bar(['PC %s' %i for i in range(0,len(var_exp))], var_exp, color ='g', label = "Explained Variance")
ax.set_title("Explained Variance")
ax.set_ylabel("Explained Variance")
ax.set_xlabel("Principal Components")
ax.legend(loc='center right', shadow=True, fontsize='large')
"""

ax2 = fig.add_subplot(1,1,1)

# Make transformation matrix
#matrix_w = eig_pairs[0][1].reshape(6,1)
matrix_w = np.hstack((eig_pairs[0][1].reshape(6,1), eig_pairs[1][1].reshape(6,1)))
print("Transformation")
print(matrix_w)

# Reproject data
y = data_std.dot(matrix_w)
print("Reprojected")
print(y)
# use this cmap
name = 'RdYlGn'
color_map=plt.get_cmap(name)
colores = getColorMap(gtcity['homicide'])
#ax2.scatter(y[:,0], [0]*len(y[:,0]), color = colores)
ax2.scatter(y[:,0],y[:,1], color = colores)



#Plot color bar
rect = 0.92,0.1,0.025,0.8
map3ax2 = fig.add_axes(rect)
latency_max = max(gtcity['homicide'])
latency_min = min(gtcity['homicide'])
ticks = np.linspace(latency_min, latency_max, 10)
norm = mpl.colors.Normalize(vmin=latency_min, vmax=latency_max)
cb5 = mpl.colorbar.ColorbarBase(map3ax2, cmap=color_map, norm=norm, orientation='vertical')
cb5.set_label('{homicides}')
cb5.set_ticks(ticks)

plt.show()
