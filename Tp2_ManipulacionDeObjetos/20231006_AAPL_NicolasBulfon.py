#           Economía Computacional
#           Trabajo práctico: Manipulación de objetos
#---------------------------------------------

#Con el archivo "AAPL.csv" que contiene información de la cotización diaria durante 5 años de las acciones de la empresa APPLE, genere un script en Spyder para realizar las siguientes operaciones de manipulación de datos.
#Una vez que redacte el Script, envíelo adjunto con el siguiente nombre: "20231006_AAPL_[NombreyApellido].py".

# Imports ->
#import scipy.stats as _stats
#import statsmodels.api as _statsModel
import pandas as _pandas
import numpy as _numpy
import matplotlib.pyplot as _plt

#1) Carga del archivo "AAPL.csv".
rutaArchivo = r'C:\\NICOLAS\FACULTAD\MATERIAS\\Cursando\Economia computacional\EconomiaComputacional_Practica\\Tp2_ManipulacionDeObjetos\\AAPL.csv';
datos = _pandas.read_csv(rutaArchivo);

#2) Indexar el archivo con la columna de fechas.
datos.set_index('Date', inplace=True);

#3) Generar un subconjunto de datos (ej. subset1) en que se muestren solamente las filas correspondientes al año 2020.
datos_2020 = datos.loc['2020-01-01':'2020-12-31'];

#4) Genere sobre el subconjunto "subset1", una estadística descriptiva de cada columna.
media_ColumnaOpen = _numpy.mean( datos_2020['Open']);
media_ColumnaClose = _numpy.mean( datos_2020['Close']);
media_ColumnaAdjClose = _numpy.mean( datos_2020['Adj Close']);

minimo_ColumnaLow = _numpy.min(datos_2020['Low']);
maximo_ColumnaHight = _numpy.max(datos_2020['High']);
varianza_ColumnaVolume = _numpy.var(datos_2020['Volume']);

#5) Obtenga un subconjunto (ej. subset2 ó dataset2) de todo el período,
# pero en que sólo se muestren las columnas de precios de apertura, cierre y volumen operado. 
#Utilice para armar el subconjunto los índices de columna Python (numéricos).
datos_apertura_cierre_volumen = datos.filter(items=['Open','Close','Volume']);

#6) En un subconjunto (ej. subset3) obtenga el valor de cierre para el día 9/11/2018.
datosDeCierre = datos.filter(items=['Date', 'Close']);
fecha = '2018-11-09';
datosDeCierreNov2018 = datosDeCierre.loc[fecha, 'Close'];

#7) Obtenga un subconjunto (ej. subset 4) para los años 2018 y 2019,
# con las columnas precio máximo, mínimo y precio de cierre ajustado.
datos_pMinimo_pMaximo_cierreAjustado = datos.filter(items=['High','Low','Adj Close']);
datos_2018_2019 = datos_pMinimo_pMaximo_cierreAjustado.loc['2018-01-01':'2019-12-31'];

#8) Genere un gráfico de líneas para todo el período considerado con el precio de cierre de la acción,
# y el precio de apertura. El gráfico deberá contener título, la leyenda de los ejes,
# como así también la leyenda del significado de cada gráfico superpuesto.

arrayFechas = datos.index;
# Selecciona un subconjunto de fechas para mostrar cada 40 dias
fechasAMostrarVisualmente = datos.index[::40];

_plt.figure(figsize=(12, 6));

_plt.plot( arrayFechas, datos['Close'], label='Precio de Cierre', color='blue');
_plt.plot( arrayFechas, datos['Open'], label='Precio de Apertura', color='green');

_plt.title('Precios de Cierre y Apertura de Apple 2018-2023');
_plt.xlabel('Fecha');
_plt.ylabel('Precio');
_plt.legend();
_plt.grid(False);

# pongo las fechas (a nivel visual) cada 40 dias para que se vea bien el grafico.
_plt.xticks(fechasAMostrarVisualmente, rotation=45);
_plt.xticks(rotation=45);
# muestro el grafico ->
_plt.show();


