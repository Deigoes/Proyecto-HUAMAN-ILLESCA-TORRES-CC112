# -*- coding: utf-8 -*-
"""Repercusión de las características técnicas de los automóviles en su eficiencia y rendimiento

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ogU79v1QKrr4_aMOpqBg3_oNd-upJm-N

<table border=1 width='140%'>
<tr>
<td bgcolor='#004261'>

# **<font color="#FFFFFF">Repercusión de las características técnicas de los automóviles en su eficiencia y rendimiento</font>**


</td>
</tr>
</table>

> La eficiencia (gasto óptimo del combustible) y el rendimiento son aspectos importantes a la hora de elegir un automóvil. Considerando ello, se realizó un análisis de un conjunto de datos que contiene las especificaciones técnicas de diversos modelos de autos, para ver como estas se relacionan con el rendimiento y la eficiencia de cada vehículo.
>
>Generalmente, un indicador de la eficiencia del auto es el parámetro mpg (millas por galón); a mayor mpg, mayor eficiencia del vehículo. Por otro lado, el indicador para el rendimiento del vehículo es la potencia del motor (hp).
"""

#Importación de librerías
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Importar el drive con el archivo csv
from google.colab import drive
drive.mount('/content/drive')

#Creamos el dataframe correpondiente al archivo csv
df_cars = pd.read_csv('/content/drive/MyDrive/proyectofunda/PARTE 3/mtcars.csv')

#Dimensión establecida como (Filas, Columnas)
print('Dimensiones de los datos = {}'.format(df_cars.shape))

#Reconocer los datos con los que vamos a trabajar nuestro análisis
df_cars.columns

""">* **model:** El modelo exacto del vehículo.
>
>* **mpg:** Abreviatura de millas por galón, característica de su efiencia.
>
>* **cyl:** Abreviatura de cilindros en línea, característica de su potencia.
>
>* **disp:** Desplazamiento en pulgadas cúbicas, entre mayor capacidad de los cilindros hay mayor compresión, y por ende, más potencia.
>
>* **hp:** Potencia (horse power)
>
>* **drat:** Número de revoluciones de la trasmisión por cada vuelta de rueda, valores altos disminuyen la eficiencia del combustible proporcionado.
>
>* **wt:** Peso del vehículo.
>
>* **qsec:** Tiempo en segundos correspondiente al desplazamiento en un cuarto de milla.
>
>* **vs:** Forma del motor, intercalado entre 1 (motor en V) y 0 (motor común).
>
>* **am:** Tipo de transmisión, intercalado entre 1 (manual) y 0 (automática)
>
>* **gear:** Número de marchas.
>
>* **carb:** Cantidad de carburadores, característica de potencia.
"""

df_cars

#filtramos el dataframe con las columnas deseadas
columnas_deseadas = ['model', 'mpg', 'cyl', 'disp', 'hp', 'wt', 'qsec','am', 'gear']
df_filt = df_cars.loc[:, columnas_deseadas]
print(df_filt)

"""<table width='140%'>
<tr>
<td bgcolor='#FDD000'>

## **<font color="#00000">Distribuciones de los atributos principales para los autos</font>**

</td>
</tr>
</table>
"""

#Resumen estadístico de los datos filtrados
df_filt.describe()

"""> Visualización de los datos


"""

#Usamos el estilo "whitegrid", con una cuadrícula blanca en el fondo del gráfico
sns.set(style="whitegrid")

#Creación de una figura con 6 subplots distribuidos en 2 filas y 3 columnas
#Tamaño de la figura: 15x10 pulgadas
#axes: matriz que contiene los ejes de cada subplot, de dimensiones 2x3
#(El conteo de filas y columnas empieza desde 0)
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))

#Histogramas
#bins: Especifica el número de contenedores para cada histograma
#kde: Muestra una curva suave para la estimación de la densidad de los datos
sns.histplot(data = df_filt, x = 'mpg', bins = 10, kde = True, ax = axes[0,0])

#Asignamos el subplot donde se graficará el histograma con su respectivo título
axes[0,0].set_title('Distribución de millas por galón')


sns.histplot(data = df_filt, x = 'disp', bins = 10, kde = True, ax = axes[0,1])
axes[0,1].set_title('Distribución de desplazamiento del motor')

sns.histplot(data = df_filt, x = 'hp', bins = 10, kde = True, ax = axes[0,2])
axes[0,2].set_title('Distribución de potencia (hp)')

sns.histplot(data = df_filt, x = 'wt', bins = 10, kde = True, ax = axes[1,0])
axes[1,0].set_title('Distribución de pesos')

sns.histplot(data = df_filt, x = 'qsec', bins = 10, kde = True, ax = axes[1,1])
axes[1,1].set_title('Distribución de tiempos (qsec)')

#Eliminar el último subplot vacío (fila 1, columna 2)
fig.delaxes(axes[1,2])

#Ajustar y mostrar los gráficos
plt.tight_layout()
plt.show()

"""<table width='140%'>
<tr>
<td bgcolor='#FDD000'>

## **<font color="#00000">Modelos mas eficientes en consumo de combustible (alto mpg)</font>**

</td>
</tr>
</table>
"""

#Mostramos los 5 modelos más eficientes
mas_eficientes = df_filt.sort_values(by = 'mpg', ascending = False)[['model', 'mpg', 'hp']].head(5)
print(mas_eficientes)

"""<table width='140%'>
<tr>
<td bgcolor='#FDD000'>

## **<font color="#00000">Modelos con mayor rendimiento (mayor HP)</font>**

</td>
</tr>
</table>
"""

#Mostramos los 5 modelos con mejor rendimiento
mejor_rendimiento = df_filt.sort_values(by = 'hp', ascending = False)[['model', 'hp', 'mpg']].head(5)
print(mejor_rendimiento)

"""<table width='140%'>
<tr>
<td bgcolor='#FDD000'>

## **<font color="#00000">Cantidad de autos por el tipo de transmisión</font>**

</td>
</tr>
</table>
"""

#Número de autos por el tipo de transmisión (am)/ 0: automático /1: manual

#Contar la frecuencia absoluta para cada valor de am
autos_transmision = df_filt['am'].value_counts()

#Creación de una figura de 8x8 pulgadas
plt.figure(figsize=(8,8))

#Título con su respectiva tipografía
plt.title('Distribución del tipo de transmisión', fontweight ="bold", fontsize = 16)

#Creación del gráfico circular
plt.pie(autos_transmision,                    #Serie que contiene la frecuencia absoluta para cada valor de am
        labels = ['Manual', 'Automático'],    #Etiquetas
        explode = [0.01,0.01],                #Separación entre las secciones del gráfico
        colors = ['#f57c73', '#b2e2f2'],      #Colores
        autopct = '%1.1f%%',                  #Muestra el porcentaje de cada sección con un decimal
        startangle = 140,                     #Ángulo inicial de la primera sección (opcional)
        textprops = {'fontsize': 14, 'fontweight':"normal"}) #Tipografía de las etiquetas

#Mostrar el gráfico
plt.show()

"""<table width='140%'>
<tr>
<td bgcolor='#FDD000'>

## **<font color="#00000">Análisis de eficiencia de combustible</font>**

</td>
</tr>
</table>

>Para analizar la eficiencia de combustible, se calcularon estadísticas resumidas como la media (mean) y la desviación estándar (std) de mpg para las categorías número de cilindros (cyl) y numero de marchas (gear)
"""

#Estadísticas de mpg por número de cilindros (cyl)
#Agrupamos todos los registros con el mismo valor en cyl y mostramos las estadísticas para la columna 'mpg
mpg_stats_por_cyl = df_filt.groupby('cyl')['mpg'].describe()
print(mpg_stats_por_cyl)

#Estadísticas de mpg por número de marchas (gear)
#Agrupamos todos los registros con el mismo valor en gear y mostramos las estadísticas para la columna 'mpg'
mpg_stats_por_gear = df_filt.groupby('gear')['mpg'].describe()
print(mpg_stats_por_gear)

"""<table width='140%'>
<tr>
<td bgcolor='#FDD000'>

## **<font color="#00000">Cantidad de autos por el número de cilindros</font>**

</td>
</tr>
</table>
"""

#Contar la frecuencia absoluta para cada valor de cyl
autos_cilindros = df_filt['cyl'].value_counts()

#Creación de una figura de 8x8 pulgadas
plt.figure(figsize=(8,8))

#Título con su respectiva tipografía
plt.title('Distribución del tipo de transmisión', fontweight ="bold", fontsize = 16)

#Creación del gráfico circular
plt.pie(autos_cilindros,                                        #Serie que contiene la frecuencia absoluta para cada valor de cyl
        labels = ['4 cilindros', '6 cilindros', '8 cilindros'], #Etiquetas
        explode=[0.01,0.01, 0.01],                              #Separación entre secciones
        colors =['#1f77b4', '#ff7f0e', '#2ca02c'],              #Selección de colores
        autopct = '%1.1f%%',                                    #Muestra el porcentaje de cada sección con un decimal
        textprops ={'fontsize': 14, 'fontweight':"normal"})     #Tipografía de las etiquetas

#Mostrar el gráfico
plt.show()

"""<table width='140%'>
<tr>
<td bgcolor='#FDD000'>

## **<font color="#00000">Cantidad de autos por el número de marchas (gear)</font>**

</td>
</tr>
</table>
"""

#Contar la frecuencia absoluta para cada valor de gear
autos_cilindros = df_filt['gear'].value_counts()

#Creación de una figura de 8x8 pulgadas
plt.figure(figsize=(8,8))

#Título con su respectiva tipografía
plt.title('Distribución del tipo de transmisión', fontweight ="bold", fontsize = 16)

plt.pie(autos_cilindros,                                        #Serie que contiene la frecuencia absoluta para cada valor de cyl
        labels = ['3 marchas', '4 marchas', '5 marchas'],       #Etiquetas
        explode = [0.01,0.01, 0.01],                            #Separación intersección
        colors = ['#9467bd', '#8c564b', '#e377c2'],             #Selección de colores
        autopct = '%1.1f%%',                                    #Muestra el porcentaje de cada sección con un decimal
        textprops = {'fontsize': 14, 'fontweight':"normal"})    #Tipografía de la etiquetas

#Mostrar el gráfico
plt.show()

"""<table width='140%'>
<tr>
<td bgcolor='#FDD000'>

## **<font color="#00000">Relación entre el desplazamiento del motor (disp) y mpg</font>**

</td>
</tr>
</table>
"""

#Importamos la función linregress de la biblioteca scipy.stats para calcular la regresión lineal
from scipy.stats import linregress

#Cálculo de la regresión lineal
slope, intercept, r_value, p_value, std_err = linregress(df_filt['disp'], df_filt['mpg'])

#Creación de una figura de tamaño 9x5 pulgadas
plt.figure(figsize=(9, 5))

#Creación del gráfico de dispersión (Etiqueta: 'autos')
plt.scatter(df_filt['disp'],df_filt['mpg'], color = 'b', label = 'autos')

#Creación de la recta de mejor ajuste (y = b + mx)
plt.plot(df_filt['disp'], intercept + slope*df_filt['disp'], color = 'red', label = 'Recta de regresión')

#Etiquetamos los ejes y el título
plt.xlabel('Desplazamiento del motor (disp)')
plt.ylabel('Millas por galón (mpg)')
plt.title('Millas por galón vs Desplazamiento del motor', fontweight ="bold")

#Mostramos la leyenda para el gráfico
plt.legend()

#Mostramos el gráfico incluyendo una cuadrícula
plt.grid(True)
plt.show()

"""<table width='140%'>
<tr>
<td bgcolor='#FDD000'>

## **<font color="#00000">Rendimiento vs eficiencia</font>**

</td>
</tr>
</table>
"""

# RELACIÓN ENTRE QSEC Y MPG
#Cálculo de la regresión lineal
slope, intercept, r_value, p_value, std_err = linregress(df_filt['qsec'], df_filt['mpg'])

#Creación de la recta de mejor ajuste (y = b + mx)
plt.plot(df_filt['qsec'], intercept + slope*df_filt['qsec'], color = 'blue')

#Creación del gráfico de dispersión con la librería seaborn
sns.scatterplot(data=df_filt, x='qsec', y='mpg', hue='gear')
plt.title('Relación entre qsec y mpg por número de marchas')
plt.xlabel('Tiempo de aceleración (qsec)')
plt.ylabel('Millas por galón (mpg)')
plt.show()

# RELACIÓN ENTRE HP Y MPG
#Parte 1
#Parámetro extra: Número de cilindros (cyl)
#Cálculo de la regresión lineal
slope, intercept, r_value, p_value, std_err = linregress(df_filt['hp'], df_filt['mpg'])

#Creación de la recta de mejor ajuste (y = b + mx)
plt.plot(df_filt['hp'], intercept + slope*df_filt['hp'], color = 'green')

#Creación del gráfico de dispersión con la librería seaborn
sns.scatterplot(data=df_filt, x='hp', y='mpg', hue='cyl')
plt.title('Relación entre hp y mpg por número de cilindros')
plt.xlabel('Caballos de fuerza (hp)')
plt.ylabel('Millas por galón (mpg)')
plt.show()

#Parte 2
#Parámetro extra: Número de marchas (gear)
#Cálculo de la regresión lineal
slope, intercept, r_value, p_value, std_err = linregress(df_filt['hp'], df_filt['mpg'])

#Creación de la recta de mejor ajuste (y = b + mx)
plt.plot(df_filt['hp'], intercept + slope*df_filt['hp'], color = 'red')

#Creación del gráfico de dispersión con la librería seaborn
sns.scatterplot(data=df_filt, x='hp', y='mpg', hue='gear')
plt.title('Relación entre hp y mpg por número de cilindros')
plt.xlabel('Caballos de fuerza (hp)')
plt.ylabel('Millas por galón (mpg)')
plt.show()

#Parte 3
#Parámetro extra: Tipo de transmisión (automática: 0, manual: 1)
#Cálculo de la regresión lineal
slope, intercept, r_value, p_value, std_err = linregress(df_filt['hp'], df_filt['mpg'])

#Creación de la recta de mejor ajuste (y = b + mx)
plt.plot(df_filt['hp'], intercept + slope*df_filt['hp'], color = 'blue')

#Creación del gráfico de dispersión con la librería seaborn
sns.scatterplot(data=df_filt, x='hp', y='mpg', hue='am')
plt.title('Relación entre hp y mpg por número de cilindros')
plt.xlabel('Caballos de fuerza (hp)')
plt.ylabel('Millas por galón (mpg)')
plt.show()