
¿Cómo dividir una columna de texto en dos columnas separadas?

df = pd.DataFrame(["STD, City State",
"33, Kolkata-West Bengal",
"44, Chennai-Tamil Nadu",
"40, Hyderabad Telengana",
"80, Bangalore Karnataka"], columns=['row'])

print(pd.DataFrame(dict(zip(range(3), [df['row'].apply(lambda x : x.split(' ')[i]) for i in range(3)]))).head())


''' ' 2) ¿Cómo obtener la frecuencia de valores repetidos en todo el dataframe?

Salida

Valores únicos listados
''' 
​

import pandas as pd

import numpy as np

df = pd.DataFrame(np.random.randint(1, 10, 20).reshape(-1, 4), columns = list('abcd'))

df

	a 	b 	c 	d
0 	7 	7 	1 	1
1 	9 	3 	7 	3
2 	7 	9 	2 	3
3 	7 	3 	3 	2
4 	7 	3 	1 	2

pd.Series(df.values.ravel()).unique()

''' array([7, 1, 9, 3, 2])''' 

#3) ¿Cómo obtener las posiciones donde coinciden los valores de dos columnas

df = pd.DataFrame({'fruit1': np.random.choice(['apple', 'orange', 'banana'], 10),
                   'fruit2': np.random.choice(['apple', 'orange', 'banana'], 10)})
arr=[]

for idx, row in df.iterrows():
    if row['fruit1'] == row['fruit2']:
        arr.extend(str(idx))

print(df)
print(arr)


''' 4) A partir de un diccionario crear un DataFrame
{‘X’:[28,35,46,50,66], 'Y':[74,84,99,13,26],'Z':[36,47,56,62,73]}
''' 
dict = {'X':[28,35,46,50,66], 'Y':[74,84,99,13,26],'Z':[36,47,56,62,73]}

dfDict = pd.DataFrame(dict)

dfDict

	X 	Y 	Z
0 	28 	74 	36
1 	35 	84 	47
2 	46 	99 	56
3 	50 	13 	62
4 	66 	26 	73


#5) Genere 3 columnas con 5 elementos cada uno. Cree una función para eliminar los N primeras o N últimas filas
df = pd.DataFrame({'fruit1': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit2': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit3': np.random.choice(['apple', 'orange', 'banana'], 5)})
print (df)
def n_primeras(df,n):
    print(df.iloc[n:])
def n_ultimas(df,n):
    print(df.iloc[:n])

n_primeras(df,2)
n_ultimas(df,2)



''' 6) Genere 5 columnas con 5 elementos cada uno. Cree una función para ordenar de forma ascendente o descendente los datos por columna.
'''
df = pd.DataFrame(np.random.randint(1, 10, 25).reshape(5, 5), columns = list('abcde'))

df

	a 	b 	c 	d 	e
0 	7 	5 	2 	6 	8
1 	7 	7 	6 	7 	6
2 	2 	6 	8 	5 	3
3 	2 	5 	6 	9 	6
4 	9 	1 	3 	9 	5

def ordenarDataFrame(df,columna,ascending):

    

    df = df.sort_values(by = columna, ascending=[ascending]) 

    #df = df.sort_index(axis=1, ascending=True)

    return df

​

df = ordenarDataFrame(df,'b',False)

​

df

​

	a 	b 	c 	d 	e
1 	7 	7 	6 	7 	6
2 	2 	6 	8 	5 	3
3 	2 	5 	6 	9 	6
0 	7 	5 	2 	6 	8
4 	9 	1 	3 	9 	5
''' 8) Genere 4 columnas con 5 elementos cada uno. Cree una función para obtener los N primeros o N ultimos registros.
''' 
df2 = pd.DataFrame(np.random.randint(1, 10, 20).reshape(5, 4), columns = list('abcd'))

df2

	a 	b 	c 	d
0 	3 	4 	3 	8
1 	8 	7 	4 	9
2 	3 	3 	5 	8
3 	4 	2 	3 	6
4 	5 	6 	9 	7

def nElementos(dataFrame,numeroDeElementos,valores):

    if(valores == 'primeros'):

        return dataFrame[:numeroDeElementos]

    elif (valores == 'ultimos'):

        return dataFrame[0-numeroDeElementos:]

    

nElementos(df2,2,'ultimos')

	a 	b 	c 	d
3 	4 	2 	3 	6
4 	5 	6 	9 	7
''' Genere 3 columnas con 5 elementos cada uno. Cree una función para obtener el numero de columnas en un dataframe.
'''
df3 = pd.DataFrame(np.random.randint(1, 10, 15).reshape(5, 3), columns = list('abc'))

df3

	a 	b 	c
0 	9 	3 	2
1 	6 	1 	9
2 	7 	1 	3
3 	7 	9 	1
4 	3 	7 	1

def numeroColumnas(df):

    return len(df.columns)

    

numeroColumnas(df3)

3

''' 12) Cree una función para crear un DataFrame a partir de una lista de listas. Suponga que la lista en la posicion 0 siempre son las cabeceras.
'''
listaDeListas = [['a','b','c'],[1,2,3],[4,5,6]]

listaDeListas

[['a', 'b', 'c'], [1, 2, 3], [4, 5, 6]]

def crearDataFrame(listaDeListas):

    df = pd.DataFrame(listaDeListas[1:],columns = listaDeListas[0])

    return df

​

crearDataFrame(listaDeListas)

	a 	b 	c
0 	1 	2 	3
1 	4 	5 	6
'''14) Escriba una funcion para eliminar los valores de numpy “inf”, “-inf” es decir Infinite Positive e Infinite negative de un dataframe por NaN. Cree un DataFrame de ejemplo para probar su funcion.
'''
df3 = pd.DataFrame(np.random.randint(1, 10, 15).reshape(5, 3), columns = list('abc'))

df3

	a 	b 	c
0 	1 	2 	2
1 	4 	6 	1
2 	1 	5 	8
3 	9 	4 	9
4 	7 	2 	6

df3 = df3.replace(1,np.inf)

df3 = df3.replace(2,np.NINF)

df3

	a 	b 	c
0 	inf 	-inf 	-inf
1 	4.000000 	6.000000 	inf
2 	inf 	5.000000 	8.000000
3 	9.000000 	4.000000 	9.000000
4 	7.000000 	-inf 	6.000000

def eliminar(df):

    df = df.replace(np.inf,np.nan)

    df = df.replace(np.NINF,np.nan)

    return df

​

eliminar(df3)

	a 	b 	c
0 	NaN 	NaN 	NaN
1 	4.0 	6.0 	NaN
2 	NaN 	5.0 	8.0
3 	9.0 	4.0 	9.0
4 	7.0 	NaN 	6.0
'''16) Escriba una funcion para ordenar un dataframe por 2 o mas columnas. Cree un DataFrame de ejemplo para probar su funcion.
'''
df3 = pd.DataFrame(np.random.randint(1, 10, 15).reshape(5, 3), columns = list('abc'))
'''
df3

	a 	b 	c
0 	8 	4 	8
1 	9 	1 	3
2 	9 	3 	7
3 	5 	1 	4
4 	6 	1 	8
'''
def ordenarPorDosoMas(df,columnas,valoresTrue):

    df = df.sort_values(columnas,ascending = valoresTrue)

    return df

ordenarPorDosoMas(df3,['a','b'],[True,True])
'''
	a 	b 	c
3 	5 	1 	4
4 	6 	1 	8
0 	8 	4 	8
1 	9 	1 	3
2 	9 	3 	7

'''


##7) Genere 4 columnas con 5 elementos cada uno. Cree una función para obtener los N primeros o N ultimos registros.
df = pd.DataFrame({'fruit1': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit2': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit3': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit4': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit5': np.random.choice(['apple', 'orange', 'banana'], 5)})
def get_n_primeras(df,n):
    print(df.iloc[:n])
def get_n_ultimas(df,n):
    print(df.iloc[n+1:])
get_n_primeras(df,2)
get_n_ultimas(df,2)


    
##9) Genere 6 columnas con 5 elementos cada uno. Cree una función para obtener un nuevo DataFrame sin la columna X
df = pd.DataFrame({'fruit1': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit2': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit3': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit4': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit5': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit6': np.random.choice(['apple', 'orange', 'banana'], 5)})
def del_column(df,column_name):
    print(df.drop(column_name, 1))

del_column(df,"fruit4")


##11) Genere 2 columnas con 20 elementos cada uno. La primera columna debe de tener uno de los siguientes valores:
##C1, C2, C3 y C4. Estos valores se pueden repetir. La segunda columna tiene valores de números cualesquiera. Cree una función para
##agrupar por la Primera Columna y que se listen los valores agrupados de la segunda Columna
df = pd.DataFrame({'column': np.random.choice(['C1', 'C2', 'C3', 'C4'], 20),