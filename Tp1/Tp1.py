# Trabajo práctico 1: Regresión Lineal Simple en Python

# Imports
import pandas as _pandas
import scipy.stats as _stats
import numpy as _numpy
import matplotlib.pyplot as _plt
import statsmodels.api as _statsModel

rutaArchivo = r'C:\\Nicolas\EconomiaComputacional\\EconomiaComputacional\\Tp1\\Table 5_10.xls';
# Paso 1: cargar datos desde un archivo Excel ->
datos = _pandas.read_excel(rutaArchivo, sheet_name='Table 5_10')


# 1) Grafique IPC en el eje vertical e IPM en el eje horizontal.
# A priori, ¿qué tipo de relación espera entre los dos índices?

ipc = datos['IPC'];
ipm = datos['IPM'];

#armo el grafico de dispersion
_plt.scatter(ipm, ipc, marker='o',color='green',label='IPC e IPM');
_plt.xlabel('IPM');
_plt.ylabel('IPC');
_plt.title('Gráfico IPC e IPM en EEUU (1980-2006)');

_plt.legend();


_plt.grid(True);
_plt.show();

# A priori, se espera un tipo de relación positiva entre los dos indices. 
#Cuando aumente el Indice de precios al consumidor, tambien debería hacerlo
# previamente el Indice de precios al productor/al por mayor.



# 2) Suponga que desea predecir un índice con base en el otro. 
# ¿Cuál utilizaría como regresada y cuál como regresora?
# Haga la regresión en Pyhton e interprete los resultados.
# Utilice el comando summary y obtenga los parámetros y el coeficiente de determinación mediante el cálculo con fórmula.

# Si deso predecir un índice con base en el otro, utilizaría al IPC como variable regresada, y al
# IPM como variable regresora. Porque en teoría se supone que al aumentar primero el IPM, eso
# empujaría al un alza consecuente en el IPC.

# Regresion:
x = ipm;
x = _statsModel.add_constant(x);
y = ipm;

regresion = _statsModel.OLS(y, x).fit();
resultados = regresion.summary();
print(resultados);

# Parámetros y Coef. de determinacion (R^2):
media_y = _numpy.mean(y);
media_x = _numpy.mean(x);

## HACER LA COVARIANZA Y LOS PARAMETROS CON FORMULA. VER LIBRO GUJARATI
covarianza = _numpy.cov(x,y);

varianza_x = _numpy.sum(x- media_x) ** 2;

beta = covarianza / varianza_x;
intercepto = media_y - beta * media_x;

# R^2
estimado_y = intercepto + beta * x;
coefDeterminacion = 1 - (_numpy.sum((y - estimado_y) ** 2) / _numpy.sum((y - media_y) ** 2))

#coefDeterminacion = _numpy.var(media_x, ddof=1) / _numpy.var(x, ddof=1);

print("Beta: "+ str(beta) + " , " + "Intercepto: "+ str(intercepto) + " , " + "R^2: " + str(coefDeterminacion));













# 3) Obtenga un gráfico final con los datos verdaderos y la recta ajustada.
# Rotule los ejes, colóquele un título al gráfico e incorpore las leyendas.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





















