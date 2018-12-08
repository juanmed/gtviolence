# Violencia Homicida en Guatemala

Este repositorio contiene datos de violencia homicida en Guatemala amablemente proporcionados por Dialogos.org.gt

El proposito es utilizar algoritmos de reconomiento de patrones y machine learning para analizar la informacion. Se ha utilizado python como lenguaje de programacion y plataforma, Pandas como herramienta para manejar la gran cantidad de informacion y SKLearn junto con algoritmos desarrollados por el autor para el analisis de los datos. 

Inicialmente, los datos en formato pdf fueron convertidos a excel utilizando ilovepdf.com. Esta pagina proveyo la mejor conversion inicial de datos a una formato utilizable para ser leidos en python utilizando la libreria pandas.

Los datos de division territorial por departament y municipio, asi como la ubicacion de caberas municipales y departamentales de Guatemala fueron descargados desde:
http://ideg.segeplan.gob.gt/

La proyeccion de estos datos, es decir, el sistema de coordenadas de referencia es EPSG42500. Este no es un sistema de coordenadas internacional, por lo que es dificil convertir de forma facil este sistema al sistema EPSG4326 que es ampliamente utilizado. Para convertir del sistema EPSG42500 en el que estan proyectados los datos, hacia EPSG4326 se utilizo el software QGIS (https://www.qgis.org/en/site/) y el archivo de proyeccion que QGIS utiliza pero con la proyeccion para Guatemala ya incluida, gracias al blog http://lenchosig.blogspot.com/2013/02/gtm-para-qgis.html.   


Los datos de matriculacion en Guatemala fueron obtenidos desde el Portal de Informacion Abierta del Ministerio de Educacion de Guatemala:
https://datosabiertos.mineduc.gob.gt/dataset/matricula-por-establecimiento

Los datos de Escuelas de Guatemala se obtuvieron de SEGEPLAN
http://www.segeplan.gob.gt/nportal/index.php/ide-descargas



