import pandas as pd
from DesafioNetflix import calculaAuto
df = pd.read_csv('ratings_small.csv', sep=',')
df_ratings = df.pivot_table(index='userId', columns='movieId', values='rating')
#Substitui os valores NaN pela média de cada coluna
df = df_ratings.fillna(df_ratings.mean())
df = df.to_numpy()
B = df.copy()
x = 100
numero_esperado = B[x-1][x-1]
B[x-1][x-1] = 1
sigma, U, V_transposto = calculaAuto(B)
B = U@sigma@V_transposto
print(f"Numero esperado: {numero_esperado}\nNumero achado: {B[x-1][x-1]}")
