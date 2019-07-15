# Violencia Homicida en Guatemala

Este repositorio contiene datos de violencia homicida en Guatemala amablemente proporcionados por Dialogos.org.gt, y scripts para trabajar con ellos ya sea [visualización](https://github.com/juanmed/gtviolence/blob/master/Graficar_data_2001_2018.ipynb) o análisis de los mismos (vendrá pronto).

![alt tag](https://github.com/juanmed/quadcopter-simulation/blob/master/content/graph1.gif)
![alt tag](https://github.com/juanmed/quadcopter-simulation/blob/master/content/vis1.gif)

Los datos se encuentran en la carpeta data:

[muertes_violentas_municipio_2001_a_2018.xlsx](https://github.com/juanmed/gtviolence/blob/master/data/muertes_violentas_municipio_2001_a_2018.xlsx): Datos de muertes violentas por departamento y municipio desde el 2001 a septiembre 2018. Obtenidos de [Dialogos.org.gt](https://drive.google.com/drive/folders/1XbOk159rR7zUri7eE1NsJBonMLAkxs8i)

El proposito es utilizar algoritmos de reconomiento de patrones y machine learning para analizar la informacion. Se ha utilizado python como lenguaje de programacion y plataforma, Pandas como herramienta para manejar la gran cantidad de informacion y pytorch, sklearn junto con algoritmos desarrollados por el autor para el análisis de los datos. 

### Antecedentes

Inicialmente, los datos en formato pdf fueron convertidos a excel utilizando ilovepdf.com. Esta página proveyo la mejor conversion inicial de datos a una formato utilizable para ser leidos en python utilizando la libreria pandas.

Los datos de division territorial por departament y municipio, asi como la ubicacion de caberas municipales y departamentales de Guatemala fueron descargados desde:
http://ideg.segeplan.gob.gt/

La proyeccion de estos datos, es decir, el sistema de coordenadas de referencia es EPSG42500. Este no es un sistema de coordenadas internacional, por lo que es dificil convertir de forma facil este sistema al sistema EPSG4326 que es ampliamente utilizado. Para convertir del sistema EPSG42500 en el que estan proyectados los datos, hacia EPSG4326 se utilizo el software QGIS (https://www.qgis.org/en/site/) y el archivo de proyeccion que QGIS utiliza pero con la proyeccion para Guatemala ya incluida, gracias al blog http://lenchosig.blogspot.com/2013/02/gtm-para-qgis.html.   


Los datos de matriculacion en Guatemala fueron obtenidos desde el Portal de Informacion Abierta del Ministerio de Educacion de Guatemala:
https://datosabiertos.mineduc.gob.gt/dataset/matricula-por-establecimiento

Los datos de Escuelas de Guatemala se obtuvieron de SEGEPLAN
http://www.segeplan.gob.gt/nportal/index.php/ide-descargas



