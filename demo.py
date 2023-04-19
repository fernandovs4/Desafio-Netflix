import pandas as pd
from DesafioNetflix import calculaAuto

df = pd.read_csv('ratings_small_formated.csv', sep=',')
#Substitui os valores NaN pela média de cada coluna
df = df.fillna(2.5)
df = df.to_numpy()
B = df.copy()
i = 238
j = 2497
numero_esperado = B[i][j]
B[i][j] = 1
sigma, U, V_transposto = calculaAuto(B)
B = U@sigma@V_transposto
print(f"Numero esperado: {numero_esperado}\nNumero achado: {B[i][j]}")
