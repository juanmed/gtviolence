# importar datos de clima

import pandas as pd
import numpy as np
import sys, os
import geopandas as gpd
import mplleaflet
import matplotlib.pyplot as plt


# importar datos GIS de departamentos y municipios y sus cabeceras
deptos = gpd.read_file("data/GIS/mapa_base_limites_departamentales_epsg4326.geojson")
muns = gpd.read_file("data/GIS/mapa_base_limites_municipales_epsg4326.geojson")
dep_cab = gpd.read_file("data/GIS/mapa_base_cabeceras_departamentales_epsg4326.geojson")
mun_cap = gpd.read_file("data/GIS/mapa_base_cabeceras_municipales_epsg4326.geojson")
# definir el sistema de coordenadas de reference
#deptos.crs = {'init' :'epsg:42500'}
#muns.crs = {'init' :'epsg:42500'}
#dep_cab.crs = {'init' :'epsg:42500'}
#mun_cap.crs = {'init' :'epsg:42500'}
# reconvertir a EPSG4326 (Latitud y longitud)
#deptos = deptos.to_crs(epsg=4326)
#muns = muns.to_crs(epsg=4326)
#dep_cab = dep_cab.to_crs(epsg=4326)
#mun_cap = mun_cap.to_crs(epsg=4326)

#print(" * Departamentos: \n{}".format(deptos.head()))
#print(" * Municipios: \n{}".format(muns.head()))
#print(" * Cabeceras Departamentales: \n{}".format(dep_cab.head()))
#print(" * Cabeceras Municipales: \n{}".format(mun_cap.head()))

year = "2010"
for (lon,lat) in zip(map(lambda p: p[0].x,dep_cab['geometry']) , map(lambda p: p[0].y,dep_cab['geometry'])):

	# You must request an NSRDB api key from the link above
	api_key = 'rrvRavEMat6yfehQnnvEpMgcCKGx8AmsJNitJ2RG'
	# Set the attributes to extract (e.g., dhi, ghi, etc.), separated by commas.
	attributes = 'ghi,dhi,dni' # ,wind_speed_10m_nwp,surface_air_temperature_nwp,solar_zenith_angle'
	# Choose year of data
	year = '2010'
	# Set leap year to true or false. True will return leap day data if present, false will not.
	leap_year = 'false'
	# Set time interval in minutes, i.e., '30' is half hour intervals. Valid intervals are 30 & 60.
	interval = '60'
	# Specify Coordinated Universal Time (UTC), 'true' will use UTC, 'false' will use the local time zone of the data.
	# NOTE: In order to use the NSRDB data in SAM, you must specify UTC as 'false'. SAM requires the data to be in the
	# local time zone.
	utc = 'false'
	# Your full name, use '+' instead of spaces.
	your_name = 'Juan+Fernando'
	# Your reason for using the NSRDB.
	reason_for_use = 'data+analysis'
	your_affiliation = 'independent+analysis'
	# Your email address
	your_email = 'juanmedrano.ec09@gmail.com'
	# Please join our mailing list so we can keep you up-to-date on new developments.
	mailing_list = 'true'

	# Declare url string
	url = 'http://developer.nrel.gov/api/solar/nsrdb_0512_download.csv?wkt=POINT({lon}%20{lat})&names={year}&leap_day={leap}&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}'.format(year=year, lat=lat, lon=lon, leap=leap_year, interval=interval, utc=utc, name=your_name, email=your_email, mailing_list=mailing_list, affiliation=your_affiliation, reason=reason_for_use, api=api_key, attr=attributes)
	# Return just the first 2 lines to get metadata:
	info = pd.read_csv(url, nrows=1)
	# See metadata for specified properties, e.g., timezone and elevation
	timezone, elevation = info['Local Time Zone'], info['Elevation']

	print(info.head())















# draw map
gt_mapa = plt.figure(figsize=(20,10))
gt_mapa_ax0 = gt_mapa.add_subplot(1,1,1)
deptos.plot(ax = gt_mapa_ax0, color = 'b', alpha = 0.5)
muns.plot(ax = gt_mapa_ax0, color = 'r', alpha = 0.5)
dep_cab.plot(ax = gt_mapa_ax0, color = 'g')
#mun_cap.plot(ax = gt_mapa_ax0, color = 'm')


for dep in np.unique(muns["departamen"]):
	temp = muns[ muns["departamen"] == dep]
	print("En "+dep+" hay "+str(len(temp["municipio"]))+" municipios")
	for mun in temp["municipio"]:
		#print(mun)
		continue






plt.show()
#mplleaflet.show()


