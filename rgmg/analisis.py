import statistics as calcular
import pandas as pd
import numpy as np
from scipy import stats

lista = ["Continua","Continua","Continua"]
lista[0]= "Discreta"
print(lista)

arreglo1 = np.array(np.random.randint(200, size=10))
arreglo2 = np.array(np.random.randint(200, size=10))
arreglo3 = np.array(np.random.randint(200, size=10))
arreglo4 = np.array(np.random.randint(200, size=10))
arreglo5 = np.array(np.random.randint(200, size=10))
arreglo6 = np.array(np.random.randint(200, size=10))

arreglo = [arreglo1,arreglo2,arreglo3,arreglo4,arreglo5,arreglo6]

ejemplo = np.var(arreglo1)
print(arreglo1)
print(arreglo2)
print("Promediox",np.cov(arreglo1))
print("Moda", stats.mode(arreglo1)[0][0])
print("Mediana",np.median(arreglo1) )

print("Varianza",np.around(ejemplo, decimals=1) )
print("Desviacion Estandar",np.around((np.std(arreglo1)), decimals = 1))
print("Maximo",max(arreglo1))
print("Minimo",min(arreglo1))
print(np.around((np.corrcoef(arreglo)), decimals= 5))