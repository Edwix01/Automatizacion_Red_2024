Para utilizar los programas presentados en este repositorio tomar en cuenta 
lo siguiente:

El primer paso seria obtener los datos de conteo de vehiculos en excel y eliminar
las primeras filas en las que se encuentran fechas, titulo, etc. De este modo
tendremos ya los numeros de conteo desde la tercera fila. 

Al tener los datos de este modo podemos usar los programas que calculan agrupan
los datos por hora y calculan las proabilidades de giro, estos programas se nombran
segun la etiqueta de cada calle, ademas se supone que habran 4 conteos por hora
(1 cada 15 minutos). Estos programas escriben los datos en un archivo de Excel
con las siguentes columnas:

H_inicio 
H_fin
N_carros
Livianos
Camiones
Probabilidad de giro 1
Probabilidad de giro 2
Probabilidad de giro 3

Al generar todos estos archivos podemos ejecutar el programa llamado flujos, 
este generara el xml de flujos necesario para jtrrouter. Este programa toma los
datos de cada hora en cada excel y crea el elemento correspondiente en xml.

Posteriormente se debera definir en un excel los ID de las calles de giro de cada
intersección, tal como se ve en el documento llamado ID_GIROS. Este excel sera 
tomado por el programa llamado Giros y junto a los documentos con los datos de
cada calle generara el archivo xml de giros necesario para jtrrouter.

Cabe mencionar que asi como se puede observar en los programas de Giros y Flujos,
al definir el nombre de los archivos de cada calle, se debe hacerlo con el ID de
la misma.

**Los archivos principales son:**

avhuaynacapac.net.xml

avhuaynacapac.poly.xml

avhuaynacapac.rou.xml

avhuaynacapac.sumo.cfg
